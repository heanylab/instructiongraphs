# parser

from lexerIG import tokens

# defines a general node in our AST
class Node(object):
  def __init__(self, kind, params):
    self.kind = kind
    self.params = params
  def print(self, tabinit):
    print(tabinit + self.kind)
    for param in self.params:
      if type(param) == float:
        print(tabinit + "  " + str(param))
      elif type(param) == str:
        print(tabinit + "  " + param)
      else:
          param.print(tabinit + "  ")
  def prettyprint(self):
    self.print("")

# parsing rules
def p_program(t):
  """program : EMPTYPROGRAM
             | PROGRAM LPAREN vdecls COMMA startdecl RPAREN"""
  if t[1] == "EmptyProgram":
    t[0] = Node("EmptyProgram", ())
  else:
    t[0] = Node("Program", (t[3], t[5]))

def p_startdecl(t):
  "startdecl : START LPAREN NUM RPAREN"
  t[0] = Node("Start", (t[3],))

def p_vdecls(t):
  """vdecls : SINGLETON LPAREN vdecl RPAREN
            | CONS      LPAREN vdecl COMMA vdecls RPAREN"""
  if t[1] == "Singleton":
    t[0] = Node("Singleton", (t[3],))
  else:
    t[0] = Node("Cons", (t[3], t[5]))

def p_vdecl(t):
  "vdecl : VERTEX LPAREN NUM COMMA vcontent RPAREN"
  t[0] = Node("Vertex", (t[3], t[5]))

def p_vcontent(t):
  """vcontent : DO          LPAREN action    COMMA vnext     RPAREN
              | DOUNTIL     LPAREN action    COMMA condition COMMA vnext RPAREN
              | CONDITIONAL LPAREN condition COMMA vnext     COMMA vnext RPAREN
              | GOTO LPAREN vnext RPAREN"""
  if t[1] == "Do":
    t[0] = Node("Do", (t[3], t[5]))
  elif t[1] == "DoUntil":
    t[0] = Node("DoUntil", (t[3], t[5], t[7]))
  elif t[1] == "Conditional":
    t[0] = Node("Conditional", (t[3], t[5], t[7]))
  else:
    t[0] = Node("GoTo", (t[3],))

def p_vnext(t):
  """vnext : END
           | NEXT LPAREN NUM RPAREN"""
  if t[1] == "End":
    t[0] = Node("End", ())
  else:
    t[0] = Node("Next", (t[3],))

def p_action(t):
  """action : MOVE LPAREN NUM    COMMA NUM COMMA NUM COMMA NUM COMMA NUM RPAREN
            | SAY  LPAREN STRING RPAREN"""
  if t[1] == "Move":
    t[0] = Node("Move", (t[3], t[5], t[7], t[9], t[11]))
  else:
    t[0] = Node("Say", (t[3],))

def p_condition(t):
  """condition : VISIBLE LPAREN STRING RPAREN
               | STOP    LPAREN NUM    COMMA  STRING RPAREN"""
  if t[1] == "Visible":
    t[0] = Node("Visible", (t[3],))
  else:
    t[0] = Node("Stop", (t[3], t[5]))

# error
def p_error(t):
  print(t)
  print("Found syntax error in input!")
  raise Exception("Parser Error")
