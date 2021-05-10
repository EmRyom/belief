from cnfConverter import *
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
    print("Revision or contraction? R or C")
    while(True):
        command = input()
        if 'r' in command.lower() or 'c' in command.lower():
            break
        if 'c' not in command.lower() and 'r' not in command.lower():
            print("Please enter R or C")
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
    resolutionres = True
    if 'r' in command.lower():
        beliefBase = revision(resolutionres,beliefBase,exp,'r')
    if 'c' in command.lower():
        beliefBase = revision(resolutionres,beliefBase,~exp,'c')
    #textBase.append(text)
    
        

        
    