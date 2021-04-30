from sympy import *
from time import sleep
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


def Biconditional(arg1, arg2):
    return((arg1>>arg2) & (arg2>>arg1)) 

def f2(exp):
    return cnf(True,exp)
def f1(exp):
    return exp
def f0(exp):
    return cnf(False,exp)


def cnf(first,exp):
    
    t = type(exp)
    if t==Symbol:
        return exp
    
    
    again = f2
    if first:
        stop = f0
    if not first:
        stop = f1
    print(exp, len(exp.args))
    
    
    if t==Or or t==And or t==Implies:
        arguments = []
        for i in range(len(exp.args)):
            arguments.append(exp.args[i])
        print(exp.args)
        print(arguments)
    
    if t==Not:
        center=exp.args[0]
    
    if t==Implies:
        return stop(~again(arguments[0]) | again(arguments[1]))
        
    if t==Not:
        if type(center)==And:
            for i in range(len(center.args)-1):
                if i==0:
                    expression = again(~center.args[0]) | again(~center.args[1])
                else:
                    expression = expression | again(~center.args[i+1])
            return stop(expression)
        if type(center)==Or:
            for i in range(len(center.args)-1):
                if i==0:
                    expression = again(~center.args[0]) & again(~center.args[1])
                else:
                    expression = expression & again(~center.args[i+1])
            return stop(expression)
        if type(center)==Not:
            return stop(center.args[0])
        return stop(~center)
    
    if t==Or:
        for i in range(len(arguments)-1):
            if i==0:
                expression = again(arguments[0]) | again(arguments[1])
            else:
                expression = expression | again(arguments[i+1])
        return to_cnf(expression)
            
    
    if t==And:
        for i in range(len(arguments)-1):
            if i==0:
                expression = again(arguments[0]) & again(arguments[1])
            else:
                expression = expression & again(arguments[i+1])
        return stop(expression)
    
    
    
    
    
    
    
print(to_cnf(( ( b >> ( ( a | ( a >> e ) ) & ( b & c ) ) ) & ~ g )) == f2(( ( b >> ( ( a | ( a >> e ) ) & ( b & c ) ) ) & ~ g )))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    