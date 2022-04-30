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
    print(variableValues)
    return tree[1]
  elif tree[0] == 'abstraction':
    variableLetter = tree[1]
    if(len(variableValues) != 0):
      if variableLetter in variableMap.keys():
        variableMap[variableLetter].append(variableValues[-1])
        variableValues.pop()
      else:
        variableMap.update({variableLetter:[variableValues[-1]]})
        variableValues.pop()
    result = eval_expression(tree[2])
    variableMap[variableLetter].pop()
    return result

#todo: change so it works with more advanced lambda expressions
def alpha_replace(tree,oldvar,newvar):  #helper
  if(tree[0] == 'abstraction'):
    if(tree[1] == oldvar):
      new_tree = [tree[0], newvar.upper(), alpha_replace(tree[2],oldvar,newvar)]
      return new_tree
    else:
      return [tree[0], tree[1], alpha_replace(tree[2],oldvar,newvar)]
  elif (tree[0] == 'application' or tree[0] == 'operation'):
    left_branch = alpha_replace(tree[1], oldvar, newvar)
    right_branch = alpha_replace(tree[2], oldvar, newvar)
    return [tree[0],left_branch,right_branch]
  elif (tree[0] == 'name'):
    if(tree[1] == oldvar):
      return [tree[0], newvar.upper()]
    else:
      return tree
  elif (tree[0] == 'num'):
    return tree

def alpha_convert(tree,var):
  if(tree[0] == 'abstraction'):
      return (alpha_replace(tree, tree[1], var)) 

#todo: change so it works with more complicated lambda expressions
def substitute(tree,var,val):
  if(tree[0] == 'abstraction'):
    new_tree = [tree[0],tree[1],substitute(tree[2],var,val)]
    return new_tree
  elif(tree[0] == 'application' or tree[0] == 'operation'):
    left_branch = substitute(tree[1], var, val)
    right_branch = substitute(tree[2], var, val)
    return [tree[0],left_branch,right_branch]
  elif(tree[0] == 'name'):
    if(tree[1] == var.upper()): #todo: add so it also evaluates that it is a free variable
      return parser.parse(val.upper()+';')
    else:
      return tree
  elif (tree[0] == 'num'):
    return tree


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
    #test:
    alpha = input('Alpha new variable: ').strip()
    print(tree)
    print('\n')
    print(alpha_convert(tree,alpha))
    print(substitute(tree,'y','(u v)'))
    #try:
    #  answer = eval_expression(tree)
    #  variableMap.clear()
    #  variableValues = []
    #  if isinstance(answer,str):
    #    print('\nEVALUATION ERROR: '+answer+'\n')
    #  else:
    #    print('\nThe value is '+str(answer)+'\n')
    #except Exception as inst:
    #  print(inst.args[0])
 
main()
