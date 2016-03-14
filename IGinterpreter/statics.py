# statics - takes an IG AST and does some static checks

from parserIG import Node

def is_program(ast):
  return type(ast) == Node \
         and (ast.kind == "EmptyProgram" or ast.kind == "Program")

def find_vertices(ast):
  if not is_program(ast):
    print("Attempted to find vertices in a non-program AST!")
    raise Exception("Statics Error")
  vertex_map = dict()
  def find_vertex_on_node(ast, vmap):
    if type(ast) != Node:
      return
    if ast.kind == "Vertex":
      vmap[ast.params[0]] = ast
    list(map(lambda node: find_vertex_on_node(node, vmap), list(ast.params)))
  find_vertex_on_node(ast, vertex_map)
  return vertex_map

def get_start_vertex(ast):
  if not is_program(ast):
    print("Attempted to get the start vertex of a non-program AST!")
    raise Exception("Statics Error")
  if ast.kind == "EmptyProgram":
    return None
  else:
    (vdecls, startdecl) = ast.params
    return startdecl.params[0]

def check_valid_start_vertex(ast, vmap):
  if not is_program(ast):
    print("Attempted to check validity of the start vertex of a non-program AST!")
    raise Exception("Statics Error")
  start_vertex = get_start_vertex(ast)
  if start_vertex != None and start_vertex not in vmap:
    print("Not a valid start vertex!")
    raise Exception("Statics Error")

def check_valid_next_vertices(ast, vmap):
  if type(ast) != Node:
    return
  if ast.kind == "Next":
    vertex_index = ast.params[0]
    if vertex_index not in vmap:
      print("Found Vertex referencing unknown vertex! Vertex index was %d"
            %vertex_index)
      raise Exception("Statics Error")
  list(map(lambda node: check_valid_next_vertices(node, vmap),
           list(ast.params)))

def check_statics(ast):
  vmap = find_vertices(ast)
  check_valid_start_vertex(ast, vmap)
  check_valid_next_vertices(ast, vmap)
