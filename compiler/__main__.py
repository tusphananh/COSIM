from interpreter.interpreter.interpreter import Interpreter
import argparse

if __name__=='__main__':
    code = open('example1.c', 'r').read()
    Interpreter.run(code)
