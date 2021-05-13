from sympy import *
a,b,c,d,e,f,g,h = symbols('a,b,c,d,e,f,g,h')


#Receives two clauses, unites them and gets rid of complementary literals
#Returns clause
def resolve(x_, y_):
    x = set(x_.copy())
    y = set(y_.copy())
    finSet = set([])
   
    for n in range(len(x)):
        element = x.pop()
        ss = set([~element])
    
        #check if there is complementary literal of x.pop in y. if not then keep in final version
        if ss.issubset(y):
            y.discard(ss.pop())
        else:
            finSet.update([element])      
    finSet.update(y)
    print("finset: ", finSet)
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
        init_clauses.remove(n)
        M_clausesImmutable = init_clauses.copy()
        
        for m in M_clausesImmutable:
            f2.add(m)
            print("1) resolve", f1, "vs: ", f2)
            ca = resolve(f1, f2)    
            
            #finSet.update(ca.copy())
            finSet = finSet.union(ca.copy())
            
            
           
            if len(ca) == 0: 
                return True
                #finSet.remove(f1.pop())
                #finSet.remove(f2.pop())
            

            if f2:
                f2.pop()
              
            
        if f1:
            f1.pop()

        
        finSet = finSet.union(init_clauses)
        
        #if there are no new clauses in final kb compared to initial kb,
        #then kb does not entail alpha
        if finSet.issubset(init_clauses):
            return False
            
        return cons
       
            
                
                
    
 
#result = resolve([c, b, a, d, ~g], [~a, ~c, g])
#print("result is ", result)


kb = set([~a|b, ~c|b, ~b])
alpha = set([a])
#print(resolution (kb,alpha))


test = eval("~a")
print("00: ", type(test))


print("\n \n ________________________________")





