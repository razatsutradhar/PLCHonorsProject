import ply.lex as lex

reserved = {'lambda': 'LAMBDA'}

tokens = ['NUMBER','LPAREN','RPAREN','OP','NAME'] + \
  list(reserved.values())

NUMBER = r'[0-9]+'
LPAREN = r'('
RPAREN = r')'
OP = r'+|-|*|/'
LAMBDA = r'[Ll][Aa][Mm][Bb][Dd][Aa]'
NAME = r'[a-zA-z][a-zA-z0-9]*'

# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  #t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()
## Test it out
#data = '''
#{with {{x 5} {y 2}} {- x y}};
#'''
#
## Give the lexer some input
#print("Tokenizing: ",data)
#lexer.input(data)
#
## Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok)
