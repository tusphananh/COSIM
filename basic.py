# TOKEN

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
DIGIT = '123456789'


class Error:
    def __init__(self, posStart, posEnd, name, detail):
        self.posStart = posStart
        self.posEnd = posEnd
        self.name = name
        self.detail = detail

    def toString(self):
        return f'{self.name} : {self.detail}' + '\n' + f'File {self.posStart.fileName} , line {self.posStart.line }'


class UnexpectedChar(Error):
    def __init__(self, posStart, posEnd, detail):
        super().__init__(posStart, posEnd, 'UnexpectedChar', detail)


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type} : {self.value}'
        return f'{self.type}'


class Position:
    def __init__(self, index, line, col, fileName, fileTXT):
        self.index = index
        self.line = line
        self.col = col
        self.fileName = fileName
        self.fileTXT = fileTXT

    def nextIndex(self, currentChar):
        self.index += 1
        self.col += 1

        if currentChar == '\n':
            self.line += 1
            self.col = 0

        return self

    def duplicate(self):
        return Position(self.index, self.line, self.col, self.fileName, self.fileTXT)


class Lexer:
    def __init__(self, fileName, text):
        self.fileName = fileName
        self.text = text
        self.pos = Position(-1, 1, -1, fileName, text)
        self.currentChar = None
        self.nextChar()

    def nextChar(self):
        self.pos.nextIndex(self.currentChar)
        self.currentChar = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def makeNum(self):
        numStr = ''
        dotCount = 0
        while self.currentChar is not None and self.currentChar in DIGIT + '.':
            if self.currentChar == '.':
                if dotCount == 1: break
                dotCount += 1
                numStr += '.'
            else:
                numStr += self.currentChar
            self.nextChar()
        if dotCount == 0:
            return Token(TT_INT, int(numStr))
        else:
            return Token(TT_FLOAT, float(numStr))

    def makeTokens(self):
        tokens = []
        while self.currentChar is not None:
            if self.currentChar in ' \t':
                self.nextChar()
            elif self.currentChar in DIGIT:
                tokens.append(self.makeNum())
                self.nextChar()
            elif self.currentChar == '+':
                tokens.append(Token(TT_PLUS))
                self.nextChar()
            elif self.currentChar == '-':
                tokens.append(Token(TT_MINUS))
                self.nextChar()
            elif self.currentChar == '*':
                tokens.append(Token(TT_MUL))
                self.nextChar()
            elif self.currentChar == '/':
                tokens.append(Token(TT_DIV))
                self.nextChar()
            elif self.currentChar == '(':
                tokens.append(Token(TT_LPAREN))
                self.nextChar()
            elif self.currentChar == ')':
                tokens.append(Token(TT_RPAREN))
                self.nextChar()
            else:
                posStart = self.pos.duplicate()
                char = self.currentChar
                self.nextChar()
                return [], UnexpectedChar(posStart, self.pos, "'" + char + "'")

        return tokens, None


def run(fileName,text):
    lexer = Lexer(fileName,text)
    tokens, errors = lexer.makeTokens()

    return tokens, errors
