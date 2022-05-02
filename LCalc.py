from LCalcParser import parser

freeVarSet = set()

def eval_tree(tree):
  if(tree[0] == 'freevars'):
    freeVarSet.clear()
    free_variable(tree[1])
    print('Free Variables: ' + str(freeVarSet))
  elif(tree[0] == 'alpha'):
    alpha(tree[1], tree[2])
    print(toString(tree[1]))
  elif(tree[0] == 'substitute'):
    tree = sub(tree[1],tree[2],tree[3])
    print(toString(tree))
  else:
    try:
        # print("beta redux exists: " + str(hasBetaReduction(tree)))
        while hasBetaReduction(tree):
            tree = applyOpRedux(tree)
            tree = applyBetaRedux(tree)
            print(toString(tree) + ";")
            tree = parser.parse(toString(tree) + ";")
            # print("beta redux exists: " + str(hasBetaReduction(tree)))
        while hasOpRedux(tree):
            tree = applyOpRedux(tree)
        print(toString(tree))
    except Exception as inst:
        print(inst.args[0])

def free_variable(tree):
    if tree[0] == 'name':  
        freeVarSet.add(tree[1])
    elif tree[0] == 'abstraction':
        free_variable(tree[2])
        freeVarSet.remove(tree[1])
    elif tree[0] == 'application':
        free_variable(tree[1])
        free_variable(tree[2])

def alpha(tree, nVar):
  if tree[0] == 'abstraction':
    oVar = tree[1]
    tree[1] = nVar
    alphaHelper(tree[2], oVar, nVar)
  elif tree[0] == 'application':
    alpha(tree[1], nVar)
  elif tree[0] == 'operation':
    alpha(tree[2], nVar)
  elif tree[0] == 'name':
    tree[0] == nVar

def alphaHelper(tree, oVar, nVar):
  if tree[0] == 'abstraction':
    if tree[1] == oVar:
      tree[1] == nVar
    alphaHelper(tree[2], oVar, nVar)
  elif tree[0] == 'application':
    alphaHelper(tree[1], oVar, nVar)
    alphaHelper(tree[2], oVar, nVar)
  elif tree[0] == 'operation':
    alphaHelper(tree[2], oVar, nVar)
    alphaHelper(tree[3], oVar, nVar)
  elif tree[0] == 'name':
    if tree[1] == oVar:
      tree[1] = nVar   

def sub(tree, oVar, nVar):
  if tree[0] == 'abstraction':
    if tree[1] == oVar:
        return tree
    else:
        tree[2] = sub(tree[2], oVar, nVar)
        return tree
  elif tree[0] == 'application':
    tree[1] = sub(tree[1], oVar, nVar)
    tree[2] = sub(tree[2], oVar, nVar)
    return tree
  elif tree[0] == 'operation':
    tree[2] = sub(tree[2], oVar, nVar)
    tree[3] = sub(tree[3], oVar, nVar)
    return tree
  elif tree[0] == 'name':
    if tree[1] == oVar:
      return nVar
    return tree 

def toString(tree):
    if (tree[0] == 'freevars'):
        return "FV [ " + str(toString(tree[1])) + " ];"
    elif (tree[0] == 'alpha'):
        return "alpha [" + str(toString(tree[2])) + ", " + str(toString(tree[3])) + " ];"
    elif (tree[0] == 'substitute'):
        return str(toString(tree[1])) + " [ " + str(toString(tree[2])) + " = " + str(toString(tree[3])) + " ];"
    elif tree[0] == 'num':
        return str(tree[1])
    elif tree[0] == 'name':
        return str(tree[1])
    elif tree[0] == 'operation':
        return "(" + str(tree[1]) + " " + str(toString(tree[2])) + " " + str(toString(tree[3])) + ")"
    elif tree[0] == 'application':
        return "(" + toString(tree[1]) + " " + str(toString(tree[2])) + ")"
    elif tree[0] == "abstraction":
        return "( lambda " + str(toString(tree[1])) + " " + str(toString(tree[2])) + ")"
    else:
        return str(tree)

def hasBetaReduction(tree):
    if tree[0] == 'num':
        return False
    elif tree[0] == 'name':
        return False
    elif tree[0] == 'operation':
        return hasBetaReduction(tree[2]) or hasBetaReduction(tree[3])
    elif tree[0] == 'application':
        return tree[1][0] == "abstraction" or hasBetaReduction(tree[1]) or hasBetaReduction(tree[2])
    elif tree[0] == "abstraction":
        return hasBetaReduction(tree[2])
    else:
        return False

def applyBetaRedux(tree):
    if tree[0] == 'num':
        return tree
    elif tree[0] == 'name':
        return tree
    elif tree[0] == 'operation':
        tree[2] = applyBetaRedux(tree[2])
        tree[3] = applyBetaRedux(tree[3])
        return tree
    elif tree[0] == 'application':
        if tree[1][0] == "abstraction":
            return alpha1(tree[1], tree[2])
        else:
            tree[1] = applyBetaRedux(tree[1])
            tree[2] = applyBetaRedux(tree[2])
            return tree
    elif tree[0] == "abstraction":
        tree[2] = applyBetaRedux(tree[2])
        return tree
    else:
        return tree

def hasOpRedux(tree):
    if tree[0] == 'num':
        return False
    elif tree[0] == 'name':
        return False
    elif tree[0] == 'operation':
        if tree[2][0] == "num" and tree[3][0] == "num":
            return True
        else:
            return hasOpRedux(tree[2]) or hasOpRedux(tree[3])
    elif tree[0] == 'application':
        return hasOpRedux(tree[1]) or hasOpRedux(tree[2])
    elif tree[0] == "abstraction":
        return hasOpRedux(tree[2])
    else:
        return False

def applyOpRedux(tree):
    if tree[0] == 'num':
        return tree
    elif tree[0] == 'name':
        return tree
    elif tree[0] == 'operation':
        if tree[2][0] == "num" and tree[3][0] == "num":
            op = tree[1]
            v1 = float(eval_expression(tree[2]))
            v2 = float(eval_expression(tree[3]))
            if op == '+':
                return ["num", v1 + v2]
            elif op == '-':
                return ["num", v1 - v2]
            elif op == '*':
                return ["num", v1 * v2]
            elif v2 != 0:
                return ["num", v1 / v2]
            else:
                return ['ERROR: Divide by Zero']
        else:
            tree[2] = applyOpRedux(tree[2])
            tree[3] = applyOpRedux(tree[3])
            return tree
    elif tree[0] == 'application':
        tree[1] = applyOpRedux(tree[1])
        tree[2] = applyOpRedux(tree[2])
        return tree
    elif tree[0] == "abstraction":
        tree[2] = applyOpRedux(tree[2])
        return tree
    else:
        return tree

def eval_expression(tree):
    if tree[0] == 'num':
        return float(tree[1])
    elif tree[0] == 'name':
        return tree[1]
    elif tree[0] == 'operation':
        op = tree[1]
        v1 = eval_expression(tree[2])
        if isinstance(v1, str):
            return v1
        v2 = eval_expression(tree[3])
        if isinstance(v2, str):
            return v2
        if op == '+':
            return v1 + v2
        elif op == '-':
            return v1 - v2
        elif op == '*':
            return v1 * v2
        elif v2 != 0:
            return v1 / v2
        else:
            return 'ERROR: Divide by Zero'
    elif tree[0] == 'application':
        outside_expr = True
        return eval_expression(beta_reduction(tree))

def beta_reduction(tree):
    if (tree[0] == 'application'):
        new_tree = alpha1(tree[1], tree[2])
        print(toString(new_tree))
        return new_tree

def alpha_helper(tree, oldvar, newvar):  
    global outside_expr
    if (tree[0] == 'abstraction'):
        if (tree[
            1] == oldvar): 
            new_tree = alpha_helper(tree[2], oldvar, newvar)
            return new_tree  
        else:
            return [tree[0], tree[1], alpha_helper(tree[2], oldvar,
                                                   newvar)] 
    elif (tree[0] == 'application'):
        left_branch = alpha_helper(tree[1], oldvar, newvar)
        right_branch = alpha_helper(tree[2], oldvar, newvar)
        return [tree[0], left_branch, right_branch]
    elif (tree[0] == 'operation'):
        left_branch = alpha_helper(tree[2], oldvar, newvar)
        right_branch = alpha_helper(tree[3], oldvar, newvar)
        return [tree[0], tree[1], left_branch, right_branch]
    elif (tree[0] == 'name'):
        if (tree[1] == oldvar):
            return newvar
        else:
            return tree
    elif (tree[0] == 'num'):
        return tree

def alpha1(tree, var):
    global outside_expr
    new_tree = tree
    if (tree[0] == 'abstraction'):  
        new_tree = (alpha_helper(new_tree, new_tree[1], var))
        return new_tree
    if (tree[0] == 'application'):
        inner = (beta_reduction(tree))
        return alpha1(inner, var)

def read_input():
    result = ''
    while True:
        data = input('LAMBDA: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i + 1]
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
        try:
            answer = eval_tree(tree)
            if isinstance(answer,str):
                print('\nEVALUATION ERROR: '+answer+'\n')
        except Exception as inst:
            print(inst.args[0])


main()
