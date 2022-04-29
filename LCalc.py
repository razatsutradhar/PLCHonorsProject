from LCalcParser import parser

def eval_expression(tree):
  print(tree)
  if tree[0] == 'num':
    return tree[1]
  elif tree[0] == 'name':
    return tree[1]
  elif tree[0] == 'operation':
    op = tree[1]
    v1 = eval_expression(tree[2])
    if isinstance(v1,str):
      return v1
    v2 = eval_expression(tree[3])
    if isinstance(v2,str):
      return v2
    if op == '+':
      return v1+v2
    elif op == '-':
      return v1-v2
    elif op == '*':
      return v1*v2
    elif v2 != 0:
      return v1/v2
    else:
      return 'ERROR: Divide by Zero'
  elif tree[0] == 'application':
    rator = eval_expression(tree[1])
    rand = eval_expression(tree[2])
    
  elif tree[0] == 'abstraction':
    input = eval_expression(tree[1])
    function = eval_expression(tree[2])
 

def read_input():
  result = ''
  while True:
    data = input('LAMBDA: ').strip() 
    if ';' in data:
      i = data.index(';')
      result += data[0:i+1]
      break
    else:
      result += data + ' '
  return result

def main():
  while True:
    data = read_input() 
    if data == 'exit;':
      break
    try:
      tree = parser.parse(data)
    except Exception as inst:
      print(inst.args[0])
      continue
    print(tree)
    try:
      answer = eval_expression(tree)
      if isinstance(answer,str):
        print('\nEVALUATION ERROR: '+answer+'\n')
      else:
        print('\nThe value is '+str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
 
main()
