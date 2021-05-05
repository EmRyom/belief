from plausibility import order
from sympy import *
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')
from copy import deepcopy



def revision(bool,bb,inp):
    if bool==True:  # Expansion
        bb.append(inp)
        return bb
    else:  # Revision
        ta = order(bb,inp)
        newbb = []
        for formula in bb:
            formula2 = deepcopy(formula)
            for i in range(len(ta[0])):
                formula2 = formula2.subs(ta[1][i],ta[0][i])
            if formula2 == True:
                newbb.append(formula)
        newbb.append(inp)
        return newbb
                
        
        







