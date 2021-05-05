from logicExpression import *
from sys import exit
from revision import revision

#print('''

# Input with 'a' and 'b' 
# Conjunction     =  a & b
# Disjunction     =  a | b
# Negation        =  ~a
# Implication     =  a >> b
# Biconditional   =  Bi (a , b)

#''')

beliefBase = []
textBase = []

def mistake():
    print("Input isn't a formula/one the of symbols isn't in the valid set of symbols")
    print("Valid symbols : {a,b,c,d,e,f,g,h}")

while(True):
    print('Belief base:')
    print(beliefBase)
    
    '''toPrint = "{"                         # Print current belief base
    if len(textBase)>0:
        toPrint+=textBase[0]
    for i in range(1,len(textBase)):
        toPrint += ", "+textBase[i]
    toPrint += "}"
    print(toPrint)'''
    
    
    print("Please enter a formula:")      # Get user input
    while(True):
        
        try:
            text=input()
            if text=="'":
                exit()
            exp=eval(text)
            cnf(True,exp)
            print("")
            break
        except NameError:
            mistake()
        except SyntaxError:
            mistake()
        except TypeError:
            mistake()
            
            
    cnfs = []                            # Transform belief base to CNF
    for i in range(len(beliefBase)):
        cnfs.append(cnf(True,beliefBase[i]))
    
    
    # This is where resolution comes into play
    beliefBase = revision(False,beliefBase,exp)
    #textBase.append(text)
    
        

        
    