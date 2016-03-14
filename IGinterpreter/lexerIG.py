# lexer

# the tokens in our IG language
tokens = [
  "LPAREN",
  "RPAREN",
  "COMMA",
  "NUM",
  "STRING",
  "EMPTYPROGRAM",
  "PROGRAM",
  "START",
  "SINGLETON",
  "CONS",
  "VERTEX",
  "DO",
  "DOUNTIL",
  "CONDITIONAL",
  "GOTO",
  "END",
  "NEXT",
  "MOVE",
  "SAY",
  "VISIBLE",
  "STOP"
]

# simple tokens
t_LPAREN =       r"\("
t_RPAREN =       r"\)"
t_COMMA =        r","
t_EMPTYPROGRAM = r"EmptyProgram"
t_PROGRAM =      r"Program"
t_START =        r"Start"
t_SINGLETON =    r"Singleton"
t_CONS =         r"Cons"
t_VERTEX =       r"Vertex"
t_DO =           r"Do"
t_DOUNTIL =      r"DoUntil"
t_CONDITIONAL =  r"Conditional"
t_GOTO =         r"GoTo"
t_END =          r"End"
t_NEXT =         r"Next"
t_MOVE =         r"Move"
t_SAY =          r"Say"
t_VISIBLE =      r"Visible"
t_STOP =         r"Stop"

# more complex tokens
def t_NUM(t):
  r"(-)?\d+(\.\d+)?"
  t.value = float(t.value)
  return t

def t_STRING(t):
  r'".*"'
  t.value = eval(t.value)
  return t

# ignore whitespace
t_ignore = " \t\n"

# error
def t_error(t):
  print("Unknown character '%s'" %t.value[0])
  print("Token: %s" %t)
  raise Exception("Lexer Error")
