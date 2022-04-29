from LCalcParser import parser

variableMap = {}
variableValues = []
def eval_expression(tree):
  if tree[0] == 'num':
    return tree[1]
  elif tree[0] == 'name':
    if tree[1] in variableMap.keys() and len(variableMap[tree[1]])>0:
      print("found variable: " + str(variableMap[tree[1]][-1]))
      return float(variableMap[tree[1]][-1])
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
  #How many different cases of application are there?
  # (x,y), (lambdaX. M)num, another application and another application
  elif tree[0] == 'application':
    variableValues.append(eval_expression(tree[2]))
    return eval_expression(tree[1])
    #elif(tree[1][0] == 'name'): #question: how do I do apply (x y)?
    #  return eval_expression(tree[1])
  elif tree[0] == 'abstraction':
    variableLetter = tree[1]
    if variableLetter in variableMap.keys():
        variableMap[variableLetter].append(variableValues[-1])
        variableValues.pop()
    else:
      variableMap.update({variableLetter:[variableValues[-1]]})
      variableValues.pop()
    result = eval_expression(tree[2])
    variableMap[variableLetter].pop()
    return result


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
