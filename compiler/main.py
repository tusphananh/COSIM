from interpreter.interpreter.interpreter import Interpreter
from interpreter.lexical_analysis.lexer import Lexer
from interpreter.syntax_analysis.parser import Parser
from interpreter.syntax_analysis.parser import SyntaxError
from interpreter.syntax_analysis.tree import *
import ast

if __name__=='__main__':
    code = open('compiler/example.c', 'r').read()
    Interpreter.run(code)

    lexer = Lexer(code)
    parser = Parser(lexer)
    viz = ast.ASTVisualizer(parser)
    content = viz.gendot()
    print(content)
