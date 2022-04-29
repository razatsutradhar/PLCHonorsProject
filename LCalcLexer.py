import ply.lex as lex

reserved = {'lambda': 'LAMBDA'}

tokens = ['NUMBER','LPAREN','RPAREN','OP','NAME','LBRACKET','RBRACKET','EQUALS','FV','ALPHA','COMMA'] + \
  list(reserved.values())

t_NUMBER = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_OP = r'\+|\-|\*|\/'
t_LAMBDA = r'[Ll][Aa][Mm][Bb][Dd][Aa]'
t_NAME = r'[a-zA-z][a-zA-z0-9]*'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'\='
t_FV = r'fv'
t_ALPHA = r'alpha'
t_COMMA = r'\,'

# Ignored characters
t_ignore = " \r\n\t;"
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
