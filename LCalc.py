from LCalcParser import parser


#unfinished. come back to later
def eval_expression(tree):
  global outside_expr
  if tree[0] == 'num':
    return float(tree[1])
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
  #How many different cases of application are there?
  # (x,y), (lambdaX. M)num, another application and another application
  elif tree[0] == 'application':
    outside_expr = True
    return eval_expression(beta_reduction(tree))


def beta_reduction(tree):
  if(tree[0] == 'application'):
    new_tree = alpha(tree[1],tree[2])
    return new_tree


#todo: change so it works with more advanced lambda expressions
def alpha_helper(tree,oldvar,newvar): #debug: doesn't work with nested lambda expressions
  #print(tree)
  #print(oldvar)
  #print(newvar)
  global outside_expr
  if(tree[0] == 'abstraction'):
    if(tree[1] == oldvar):
      new_tree = alpha_helper(tree[2],oldvar,newvar)
      return new_tree #only executes when we have the final product
    else:
      return [tree[0], tree[1],alpha_helper(tree[2],oldvar,newvar)] # only triggers when we have an inner abstraction
  elif (tree[0] == 'application'):
    left_branch = alpha_helper(tree[1], oldvar, newvar)
    right_branch = alpha_helper(tree[2], oldvar, newvar)
    return [tree[0],left_branch,right_branch]
  elif(tree[0] == 'operation'):
    left_branch = alpha_helper(tree[2], oldvar, newvar)
    right_branch = alpha_helper(tree[3], oldvar, newvar)
    return [tree[0],tree[1],left_branch,right_branch]
  elif (tree[0] == 'name'): #we're returning the sub-branch of the tree, not the value
    if(tree[1] == oldvar):
      return newvar
    else:
      return tree
  elif (tree[0] == 'num'):
    return tree

def alpha(tree,var):
  global outside_expr
  new_tree = tree
  if(tree[0] == 'abstraction'): #this should deal with nested lambda expressions?
    if((alpha_helper(new_tree, new_tree[1], var))[0] == 'abstraction'):
      new_tree = (alpha_helper(new_tree, new_tree[1], var))
    else:
      new_tree = (alpha_helper(new_tree, new_tree[1], var))
    return new_tree
  if(tree[0] == 'application'):
    inner = (beta_reduction(tree))
    return alpha(inner,var)

#todo: change so it works with more complicated lambda expressions
def substitute(tree,var,val):
  if(tree[0] == 'abstraction'):
    new_tree = [tree[0],tree[1],substitute(tree[2],var,val)]
    return new_tree
  elif(tree[0] == 'application'):
    left_branch = substitute(tree[1], var, val)
    right_branch = substitute(tree[2], var, val)
    return [tree[0],left_branch,right_branch]
  elif(tree[0] == 'operation'):
    left_branch = substitute(tree[2], var, val)
    right_branch = substitute(tree[3], var, val)
    return [tree[0],left_branch,right_branch]
  elif(tree[0] == 'name'):
    if(tree[1] == var.upper()): #todo: add so it also evaluates that it is a free variable
      return parser.parse(val.upper()+';') #here val isn't a tree yet so we need to turn it into a tree
    else:
      return tree
  elif (tree[0] == 'num'):
    return tree

#todo: change so it works with more complicated lambda expressions
def free_variable_helper(tree, bound_var):
  if(tree[0] == 'abstraction'):
    free_variable(tree)
  elif(tree[0] == 'application' or tree[0] == 'operation'):
    left_branch = free_variable_helper(tree[1], bound_var)
    right_branch = free_variable_helper(tree[2], bound_var)
    for i in range (len(right_branch)):
      left_branch.append(right_branch[i])
    return left_branch
  elif (tree[0] == 'name'):
    if(tree[1] != bound_var):
      return tree[1]
    else:
      return []
  elif (tree[0] == 'num'):
    return []

#finds the free variable of a single individual lambda expression. nothing more nothing less
def free_variable(tree):
  if(tree[0] == 'abstraction'):
    bound_variable = tree[1]
    return free_variable_helper(tree[2],bound_variable)


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
    print(tree)
    print('\n')
    print(beta_reduction(tree))
    try:
      answer = eval_expression(tree)
      if isinstance(answer,str):
        print('\nEVALUATION ERROR: '+answer+'\n')
      else:
        print('\nThe value is '+str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
 
main()
