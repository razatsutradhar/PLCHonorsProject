import ply.yacc as yacc
from LCalcLexer import tokens

#( lambda x ( + x x ) 5 );
def p_expr_1(p):
  'expr : NUMBER'
  p[0] = ['num', p[1]]

def p_expr_2(p):
  'expr : NAME'
  p[0] = ['name', p[1]]

def p_expr_3(p):
  'expr : LPAREN expr RPAREN'
  p[0] = p[2]

def p_expr_4(p):
  'expr : LPAREN expr expr RPAREN'
  p[0] = ['application', p[2], p[3]]

def p_expr_5(p):
  'expr : LAMBDA NAME expr'
  p[0] = ['abstraction', p[2], p[3]]

def p_expr_6(p):
  'expr : LPAREN OP expr expr RPAREN'
  p[0] = ['operation', p[2], p[3], p[4]]



def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()

# (
#   (
#     (
#       (
#         lambda x (
#           lambda y (
#             lambda z (* (x z) (y z)
#             )
#           )
#         )
#       )
#       (lambda x (* x x))
#     )
#     (lambda x (+ x x))
#   )
# 5
# );