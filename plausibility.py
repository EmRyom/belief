
from sympy import *
import numpy as np
from copy import deepcopy 
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


def variables(bb):
    
    syms = set()
    for b in bb:
        syms = syms.union(b.atoms())
        
    return syms

def truthassignments(n):
    i = [[True, False]]
    for u in range(1,n):
        l = len(i[0])
        i = np.hstack((i,i))
        newColumn = flatten([[True]*l,[False]*l])
        i = np.vstack((i,newColumn))
    return np.transpose(i)


def order(bb,inp):
    var = list(variables(bb).union(variables([inp])))
    truthtable = truthassignments(len(var))
    
    plaus = []
    
    for assignment in truthtable:            
        correct = 0
        for formula in bb:
            formula2 = deepcopy(formula)
            for i in range(len(assignment)):
                formula2 = formula2.subs(var[i],assignment[i])
            if formula2 == True:
                correct +=1
        formula2 = deepcopy(inp)
        for i in range(len(assignment)):
            formula2 = formula2.subs(var[i],assignment[i])
        if formula2 == True:
            plaus.append((correct,assignment,var))
    m = 0
    best = []
    for i in range(len(plaus)):
        if plaus[i][0]>m:
            best = plaus[i]
            m = plaus[i][0]
    return (best[1],best[2])
                
                
                
    
    

