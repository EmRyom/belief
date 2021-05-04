from sympy import *
from time import sleep
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


def Bi(arg1, arg2): # Biconditional
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
        #print(exp.args)
        #print(arguments)
    
    if t==Implies:
        return stop(~again(arguments[0]) | again(arguments[1]))
        
    if t==Not:
        center=exp.args[0]
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
        # checks whether distributive law needs to be applied
        dist_law = 0
        for arg in arguments:
            if (type(arg)==And):
                dist_law = 1
        
        if dist_law == 1:
            subexp = []
            for i in range(len(arguments)):
                helper = []
                if type(arguments[i])==And:
                    for arg in arguments[i].args:
                        if subexp == []:
                            helper.append(again(arg))
                        else:
                            for subarg in subexp:
                                helper.append(subarg | again(arg))
                    subexp = helper
                else:
                    if subexp == []:
                        subexp.append(again(arguments[i]))
                    else:
                        for subarg in subexp: 
                            subexp.append(subarg | again(arguments[i]))
            
            for i in range (len(subexp)):
                if i==0:
                    expression = subexp[i]
                else:
                    expression = expression & subexp[i]
                    
        else:
            for i in range(len(arguments)-1):
                if i==0:
                    expression = again(arguments[0]) | again(arguments[1])
                else:
                    expression = expression | again(arguments[i+1])
                    
        return expression
            
    
    if t==And:
        for i in range(len(arguments)-1):
            if i==0:
                expression = again(arguments[0]) & again(arguments[1])
            else:
                expression = expression & again(arguments[i+1])
        return stop(expression)
    
    
    
    
    
    
#print(f2(c | (a & b) | (d & g)))   
print(to_cnf(( ( b >> ( ( a | ( a >> e ) ) & ( b & c ) ) ) & ~ g )) == f2(( ( b >> ( ( a | ( a >> e ) ) & ( b & c ) ) ) & ~ g )))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    