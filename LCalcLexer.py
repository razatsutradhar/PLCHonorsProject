import ply.lex as lex

reserved = {'lambda': 'LAMBDA', 'fv':'FV', 'alpha':'ALPHA'}

tokens = ['NUMBER','LPAREN','RPAREN','OP','NAME','LBRACKET','RBRACKET','EQUALS','COMMA','SEMI'] + \
  list(reserved.values())


def t_NUMBER(t):
  r'[-+]?[0-9]+(\.([0-9]+)?)?'
  t.value = float(t.value)
  t.type = 'NUMBER'
  return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_OP = r'\+|\-|\*|\/'
t_LAMBDA = r'[Ll][Aa][Mm][Bb][Dd][Aa]'


def t_NAME(t):
  r'[a-zA-Z][_a-zA-Z0-9]*'
  t.type = reserved.get(t.value.lower(), 'NAME')
  return t


t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'\='
t_FV = r'fv'
t_ALPHA = r'alpha'
t_COMMA = r'\,'
t_SEMI = r'\;'

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
