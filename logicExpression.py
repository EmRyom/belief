from sympy import *
from time import sleep
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')

def f2(exp):
    return cnf(True,exp)
def f1(exp):
    return exp
def f0(exp):
    return cnf(False,exp)

def integ(exp):
    t=type(exp)
    ar=exp.args
    le=len(ar)
    if le==2:
        return t(ar[0],ar[1])
    if le==1:
        return t(ar[0])
    
    if le>2:
        return t(ar[0],t(ar[1],ar[1:]))
    if True:
        print("WTF")

def cnf(first,exp):
    
    t = type(exp)
    if t==Symbol:
        return exp
    
    
    exp=integ(exp)
    
    
    again = f2
    if first:
        stop = f0
    if not first:
        stop = f1
    print(exp, len(exp.args))
    sleep(1)
    
    
    if t==Or or t==And or t==Implies:
        left=exp.args[0]
        print(exp.args)
        right=exp.args[1]
    
    if t==Not:
        center=exp.args[0]
    
    if t==Implies:
        return stop(~again(left) | again(right))
        
    if t==Not:
        if type(center)==And:
            return stop(again(~center.args[0]) | again(~center.args[1]))
        if type(center)==Or:
            return stop(again(~center.args[0]) & again(~center.args[1]))
        if type(center)==Not:
            return stop(center.args[0])
        return stop(~center)
    
    if t==Or:
        if type(right)==And:
            return stop(again(left | right.args[0]) & again(left | right.args[1]))
        if type(left)==And:
            return stop(again(left.args[0] | right) & again(left.args[1] | right))
        return stop(again(left) | again(right))
    
    if t==And:
        return stop(again(left) & again(right))
    
    
    
    
    
    
    
to_cnf(( ( b >> ( ( a | ( a >> e ) ) & ( b & c ) ) ) & ~ g )) == f2(( ( b >> ( ( a | ( a >> e ) ) & ( b & c ) ) ) & ~ g ))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    