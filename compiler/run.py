from interpreter.interpreter.interpreter import Interpreter
from interpreter.lexical_analysis.lexer import Lexer
from interpreter.syntax_analysis.parser import Parser
from interpreter.syntax_analysis.parser import SyntaxError
from interpreter.syntax_analysis.tree import *
import ast
from compiler.__main__ import MainFrame
class Run(object):
    def __init__(self):
        pass

if __name__=='__main__':
    code1 = open("D:\\Code\example1.c", 'r').read()
    Interpreter.run(code1)
