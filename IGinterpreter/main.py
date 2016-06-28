#!/usr/bin/env python2
# main driver to interpret IGs

import ply.lex as lex
import lexerIG
import ply.yacc as yacc
import parserIG
import statics
import dynamics
import init

import sys

lexer = lex.lex(module=lexerIG)
parser = yacc.yacc(module=parserIG)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Use: main.py <IG program>"
    exit(1)
    init.initialize()
  try:
    igfile = open(sys.argv[1], "r")
    igcode = igfile.read()
  except Exception as e:
    print e
    print "Could not open file for reading!"
    exit(1)
  ast = parser.parse(igcode)
  assert(statics.valid(ast))
  dynamics.eval(ast)
  igfile.close()
