#forward chaining in artificial intelligence 

'''Knowledge Base in Horn Form

P=>Q
L^M=>P
B^L=>M  
A^B=>L
A
B

'''

with open('banner.txt','r') as file:
    for line in file:
        print(line,end='')
    print('\n')


'''Function that reads knowledge base from file'''

def read_knoweledge_base(filename):
    kb = []
    facts=[]

    with open(filename,'r') as file:
        for line in file:
            rule = line.strip().split('=>')
            if len(rule) == 1:
                fac = rule[0].strip()
                facts.append(fac)
            else:
                consequent = rule[1].strip()
                antecedents = rule[0].split('^')
                antecedents = [antecedent.strip() for antecedent in antecedents]
                kb1={"antecendts":antecedents,"consequent":consequent}
                kb.append(kb1)
    return kb,facts



'''Forward Chaining'''

'''While loop until there is no new facts were derived
Perform Forward Chaining'''

# def forward(facts,knowledge_base):
#     facts = set(facts)
#     while True:
#         new_facts=set()
#         for rule in knowledge_base:
#             if all(x in facts for x in rule["antecendts"]):
#                 new_facts.update(rule["consequent"])
#         if not new_facts.difference(facts):
#             '''Break the loop if there will be no new facts were defined'''
#             break
        
#         facts.update(new_facts)

#     return facts

def forward(facts, knowledge_base):
    facts = set(facts)
    
    while True:
        new_facts = set()
        for rule in knowledge_base:
            if all(a in facts for a in rule['antecendts']):
                new_facts.add(rule['consequent'])
        
        if not new_facts.difference(facts):
            break
        
        facts.update(new_facts)
    
    return facts




    

'''The final list after performing Forward Chaining'''

print("\n***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&**\n")
print("-------------------------------- Results after performing forward chaining -----------------------------------\n")

knowledge_base2,facts2 = read_knoweledge_base('kb.txt')
re1 = forward(facts2,knowledge_base2)
if re1:
    for i in re1:print(i,end="  ")
    print(" - all this facts can be proven using initial facts:")
    for item in knowledge_base2:
        if item['consequent'] in re1:
            if type(item) == str:
                print(f"- {item}")
            else:
                print(f"- {' and '.join(item['antecendts'])} => {item['consequent']}")



'''Backward Chaining'''

with open('banner1.txt','r') as file:
    for line in file:
        print(line,end='')
    print('\n')

'''Function for Backward Chaining that use recursion to 
determine that goal is possible to derive from given knowledge base'''

def backward(goal, rules, facts, path=[]):
    # Check if the goal is already a fact
    if goal in facts:
        path.append(goal)
        return True, path
    
    # Check if the goal can be inferred from existing facts using a rule
    for rule in rules:
        if goal == rule["consequent"]:
            # Check if all the antecedents of the rule can be satisfied
            satisfied = True
            for antecedent in rule["antecendts"]:
                antecedent_proven, path = backward(antecedent, rules, facts, path)
                if not antecedent_proven:
                    satisfied = False
                    break
            if satisfied:
                # If all antecedents are satisfied, add the consequent as a fact and return True
                path.append(rule)
                facts.append(rule["consequent"])
                return True, path
    
    # If none of the rules can satisfy the goal, return False
    return False, path


print("\n***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&**\n")
print("-------------------------------- Results after performing backward chaining -----------------------------------\n")

knowledge_base3,facts3 = read_knoweledge_base('kb.txt')
print("------- Enter the Sentence that you want to Derive ------ ")
goal = str(input())


result, path = backward(goal, knowledge_base3, facts3)
if result:
    print(f"{goal} can be proven using the following facts and rules:")
    for item in path:
        if type(item) == str:
            print(f"- {item}")
        else:
            print(f"- {' and '.join(item['antecendts'])} => {item['consequent']}")
else:
    print(f"{goal} cannot be proven using the existing facts and rules.")