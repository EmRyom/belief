from sympy import *
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


def addDisjunBack(finSet):  
    finString = ''
    for el in finSet:
        finString += str(el) + "|" 
    finString = finString[:-1]
    evalStr = eval(finString)
    result = set([evalStr])
    return result


#split to sentences e.g {a|~b} into a (a,~b)
def splitClause(x_):
    x = set([])
    if len(x_) > 0:
        xx = eval(str(list(x_.copy())[0]))
        if len (xx.args) == 0: 
            x.add(xx)
        
        if len(xx.args) == 1 and type(xx) == Not:
            x.add(xx)
        
        if len(xx.args) > 1:
            for i in range(len(xx.args)):
                x.add(xx.args[i])
    return x
    


#Receives two clauses, unites them and gets rid of complementary literals
#Returns clause
def resolve(x_, y_):
    x = splitClause(x_)
    y = set(y_.copy())
    finSet = set([]) 
    
    for n in range(len(x)):      
        element = x.pop()
        ss = set([~element])
        if ss.issubset(splitClause(y)):
            ssTemp = ss.pop()
            yyy = splitClause(y)
            yyy.discard(ssTemp)
            y = yyy
            
        else:
            finSet.update([element])    
            
    if len(finSet) > 0: 
        finSet = addDisjunBack(finSet)  
    finSet.update(y)
    return finSet



#Receives knowledge base and formula alpha
#gets through all formulas
def resolution (kb_,alpha_):  
    kb = set(kb_.copy())
    alpha = set(alpha_.copy())
    init_clauses = kb.union(alpha)
    finSet = set([])
    prevFinSet= set([])
    
    
    while True:
        N_clausesImmutable = init_clauses.copy()
        f1, f2 = set([]), set([])
         
        for n in N_clausesImmutable:
            f1.add(n)
            init_clauses.discard(n)
            M_clausesImmutable = init_clauses.copy()
            
            for m in M_clausesImmutable:    
                f2.add(m)
                ca = resolve(f1, f2)    
                finSet = finSet.union(ca.copy())
    
                if len(ca) == 0: 
                    return True
    
                if f2:
                    f2.pop()
                  
                
            if f1:
                f1.pop()
     
            
        #if could did not found empty clause that was yield, and the final Set
        #is same as in prev iteration
        if len(prevFinSet)>0 and prevFinSet==finSet:
            return False
        
        finSet = finSet.union(init_clauses)
        init_clauses = init_clauses.union(finSet)
        prevFinSet = finSet


   
            

####
#kbE = set([~a|b|c,~b|a,~c|a,~a])
#alphaE = set([b])

kbF = set([~a|b, c])
kbT = set([~a|b, ~c|b, c])
alpha = set([~b])
resol = resolution (kbT,alphaT)

print("Resolution: \n");
if resol:
    print("True. KB entails alpha")
else:
    print("False. KB does not entail alpha")


