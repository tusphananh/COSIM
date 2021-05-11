from compiler.interpreter.interpreter.interpreter import Interpreter
from compiler.interpreter.lexical_analysis.lexer import Lexer
from compiler.interpreter.syntax_analysis.parser import Parser
from compiler.interpreter.syntax_analysis.parser import SyntaxError
from compiler.interpreter.syntax_analysis.tree import *
import ast

if __name__=='__main__':
    code = open('example.c', 'r').read()
    Interpreter.run(code)

    lexer = Lexer(code)
    parser = Parser(lexer)
    viz = ast.ASTVisualizer(parser)
    content = viz.gendot()
    print(content)
