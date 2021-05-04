import numpy as np
from sympy import *
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


def collect(exp):
    
    
    t = type(exp)
    
    if t == Symbol:
        return exp
    
    if t == And or t == Or:
        return [collect(arg) for arg in exp.args]
    
    if t == Implies:
        return [collect(arg) for arg in exp.args]
    
    if t == Not:
        some = exp.args
        nots = []
        for lis in some:
            for arg in lis:
                nots.append(np.array(Not(some)).flatten())
        
        return nots
    
    
    