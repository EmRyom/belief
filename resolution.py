from sympy import *
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


def addDisjunBack(finSet):  
    finString = ''
    for el in finSet:
        finString += str(el) + "|" 
    finString = finString[:-1]
    evalStr = eval(finString)
    #print("evalStr ", evalStr)
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
    #print("x= ", x_,"    y= ", y_)
    x = splitClause(x_)
    y = set(y_.copy())
    finSet = set([]) 
    
    for n in range(len(x)):
              
        element = x.pop()
        ss = set([~element])
        
        
        
        #print("subset: ", ss.issubset(splitClause(y) ))
        

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
    #print ("finset: ", finSet , "\n")
    return finSet



#Receives knowledge base and formula alpha
#gets through all formulas
def resolution (kb_,alpha_):  
    kb = set(kb_.copy())
    alpha = set(alpha_.copy())
    
    #same as kb | alpha
    init_clauses = kb.union(alpha)
    cons = False
    finSet = set([])
    
    
    N_clausesImmutable = init_clauses.copy()
    f1, f2 = set([]), set([])
    
    
   
    for n in N_clausesImmutable:
        f1.add(n)
        init_clauses.discard(n)
        M_clausesImmutable = init_clauses.copy()
        
        for m in M_clausesImmutable:
            f2.add(m)
            print("f1==", f1, "vs: f2==", f2)
            ca = resolve(f1, f2)    
            
            print(" ca : ", ca)
            #finSet.discard({b})
            #finSet.discard(f2)
          
            finSet = finSet.union(ca.copy())
            
            #INSTEAD OF DELETING FROM FINSET, WE ACTUALLY NEED TO DELETE FROM initial_clauises
            f1safe = f1.pop()
            finSet.discard(f1safe)
            f1.update([f1safe])
            
            f2safe = f2.pop()
            finSet.discard(f2safe)
            f2.update([f2safe])
            
            print("    finSet: ", finSet ,"\n")
            
           
            if len(ca) == 0: 
                return True
                #finSet.remove(f1.pop())
                #finSet.remove(f2.pop())
            

            if f2:
                f2.pop()
              
            
        if f1:
            f1.pop()

        
    finSet = finSet.union(init_clauses)
    print ("== finSet", finSet) 
    
    #print("finset: ", finSet, "   vs   init_clauses: ", init_clauses)
    #if there are no new clauses in final kb compared to initial kb,
    #then kb does not entail alpha
    if finSet.issubset(init_clauses):
        return False
            
        
        #return cons
   
            
                
                
    
 
#result = resolve([c, b, a, d, ~g], [~a, ~c, g])
#print("result is ", result)

kbb = set([a|~c, b])
#kb = set([~a|b, ~c|b, ~b])
alpha = set([c])
print("Resoluition: ", resolution (kbb,alpha))

t = set([a|~c])
#resolve(t,alpha)

'''
yyx = splitClause(t)
print("yyx ",yyx)
print("alpha is subset of y?", alpha.issubset(yyx))
'''
