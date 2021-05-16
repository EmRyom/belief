from plausibility import order
from sympy import *
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')
from copy import deepcopy


def checkFormula(bb,ta):
    newbb = set()
    for formula in bb:
        formula2 = deepcopy(formula)
        for i in range(len(ta[0])):
            formula2 = formula2.subs(ta[1][i],ta[0][i])
        if formula2 == True:
            newbb.add(formula)
    return newbb


def revision(bool,bb,inp,command):
    if command=='r':
        if bool==True or len(bb) == 0 :  # Expansion
            if not (inp in bb):
                bb.append(inp)
            return bb
        else:  # Revision
            ta = order(bb,inp)
            newbb = checkFormula(bb,ta)
            newbb.add(inp)
            return list(newbb)
    else:  # Contraction
        if bool==False:
            return bb
        else:
            tao = order(bb,bb[0])
            bbo = checkFormula(bb,tao)
                    
            tan = order(bb,inp)
            bbn = checkFormula(bb,tan)
            return list(bbn.intersection(bbo))
            
                
        
        







