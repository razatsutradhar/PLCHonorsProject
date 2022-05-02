
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALPHA COMMA EQUALS FV LAMBDA LBRACKET LPAREN NAME NUMBER OP RBRACKET RPAREN SEMIexprStart : expr SEMIexprStart : expr LBRACKET NAME EQUALS expr RBRACKET SEMIexprStart : FV LBRACKET expr RBRACKET SEMIexprStart : ALPHA LBRACKET expr COMMA NAME RBRACKET SEMIexpr : NUMBERexpr : NAMEexpr : LPAREN expr expr RPARENexpr : LPAREN LAMBDA NAME expr RPARENexpr : LPAREN OP expr expr RPARENexpr : LPAREN expr RPAREN'
    
_lr_action_items = {'FV':([0,],[4,]),'ALPHA':([0,],[5,]),'NUMBER':([0,3,6,7,10,11,12,14,19,20,21,22,25,31,32,],[6,-6,-5,6,6,6,6,6,-10,6,6,6,-7,-8,-9,]),'NAME':([0,3,6,7,9,10,11,12,13,14,19,20,21,22,24,25,31,32,],[3,-6,-5,3,15,3,3,3,20,3,-10,3,3,3,30,-7,-8,-9,]),'LPAREN':([0,3,6,7,10,11,12,14,19,20,21,22,25,31,32,],[7,-6,-5,7,7,7,7,7,-10,7,7,7,-7,-8,-9,]),'$end':([1,8,29,35,36,],[0,-1,-3,-2,-4,]),'SEMI':([2,3,6,19,23,25,31,32,33,34,],[8,-6,-5,-10,29,-7,-8,-9,35,36,]),'LBRACKET':([2,3,4,5,6,19,25,31,32,],[9,-6,10,11,-5,-10,-7,-8,-9,]),'RPAREN':([3,6,12,18,19,25,26,27,31,32,],[-6,-5,19,25,-10,-7,31,32,-8,-9,]),'RBRACKET':([3,6,16,19,25,28,30,31,32,],[-6,-5,23,-10,-7,33,34,-8,-9,]),'COMMA':([3,6,17,19,25,31,32,],[-6,-5,24,-10,-7,-8,-9,]),'LAMBDA':([7,],[13,]),'OP':([7,],[14,]),'EQUALS':([15,],[22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exprStart':([0,],[1,]),'expr':([0,7,10,11,12,14,20,21,22,],[2,12,16,17,18,21,26,27,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exprStart","S'",1,None,None,None),
  ('exprStart -> expr SEMI','exprStart',2,'p_exprStart_1','LCalcParser.py',5),
  ('exprStart -> expr LBRACKET NAME EQUALS expr RBRACKET SEMI','exprStart',7,'p_exprStart_2','LCalcParser.py',9),
  ('exprStart -> FV LBRACKET expr RBRACKET SEMI','exprStart',5,'p_exprStart_3','LCalcParser.py',13),
  ('exprStart -> ALPHA LBRACKET expr COMMA NAME RBRACKET SEMI','exprStart',7,'p_exprStart_4','LCalcParser.py',17),
  ('expr -> NUMBER','expr',1,'p_expr_1','LCalcParser.py',22),
  ('expr -> NAME','expr',1,'p_expr_2','LCalcParser.py',26),
  ('expr -> LPAREN expr expr RPAREN','expr',4,'p_expr_3','LCalcParser.py',30),
  ('expr -> LPAREN LAMBDA NAME expr RPAREN','expr',5,'p_expr_4','LCalcParser.py',34),
  ('expr -> LPAREN OP expr expr RPAREN','expr',5,'p_expr_5','LCalcParser.py',38),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_6','LCalcParser.py',42),
]