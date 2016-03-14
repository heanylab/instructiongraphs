# interpreter - executes an IG

from statics import is_program, find_vertices, get_start_vertex
import time

def execute_action(action):
  if action.kind == "Move":
    (a, b, c, d, e) = action.params
    print("Moving with parameters (%s, %s, %s, %s, %s)" %(a, b, c, d, e))
    time.sleep(action.params[0] / 2)
  elif action.kind == "Say":
    print("Robot says: '%s'" %action.params[0])
    time.sleep(1)

def execute_condition(condition):
  if condition.kind == "Visible":
    print("Checking if %s is visible..." %condition.params[0])
    time.sleep(1)
    print("Is %s visible?" %condition.params[0])
    ans = input()
    return ans in ("yes", "y", "", "\n")
  elif condition.kind == "Stop":
    print("Checking if %s is within %s distance..." %(condition.params[1],
                                                      condition.params[0]))
    time.sleep(1)
    print("Is %s within %s distance?" %(condition.params[1],
                                        condition.params[0]))
    ans = input()
    return ans in ("yes", "y", "", "\n")

def execute_content(content):
  if content.kind == "Do":
    (action, vnext) = content.params
    execute_action(action)
    return vnext
  elif content.kind == "DoUntil":
    (action, condition, vnext) = content.params
    execute_action(action)
    while(not execute_condition(condition)):
      execute_action(action)
    return vnext
  elif content.kind == "Conditional":
    (condition, vnext1, vnext2) = content.params
    if execute_condition(condition):
      return vnext1
    else:
      return vnext2
  elif content.kind == "GoTo":
    (vnext,) = content.params
    return vnext

def execute(ast):
  if not is_program(ast):
    print("Attempted to execute a non-program AST!")
    raise Exception("Runtime Error")
  if ast.kind == "EmptyProgram":
    print("Finished.")
    return
  start_vertex_index = get_start_vertex(ast)
  vmap = find_vertices(ast)
  curr_vertex = vmap[start_vertex_index]
  (_, curr_content) = curr_vertex.params
  vnext = execute_content(curr_content)
  while (vnext.kind != "End"):
    curr_vertex_index = vnext.params[0]
    curr_vertex = vmap[curr_vertex_index]
    (_, curr_content) = curr_vertex.params
    vnext = execute_content(curr_content)
  print("Finished.")
