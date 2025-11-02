# #forward chaining in artificial intelligence 



# with open('banner.txt','r') as file:
#     for line in file:
#         print(line,end='')
#     print('\n')


# '''Function that reads knowledge base from file'''

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


                # kb.setdefault(consequent,[]).append(antecedents)

    return kb,facts
#     kb = {}

#     with open(filename,'r') as file:
#         for line in file:
#             rule = line.strip().split('=>')

#             if len(rule) == 1:
#                 fact = rule[0].strip()
#                 kb.setdefault(fact,[])
#             else:
#                 consequent = rule[1].strip()
#                 antecedents = rule[0].split('^')
#                 antecedents = [antecedent.strip() for antecedent in antecedents]
#                 for ant in antecedents:
#                     kb.setdefault(ant,[]).append(consequent)

#     return kb



'''Forward Chaining'''

'''The defined knowledge base as a dictionary'''

knowledge_base2,facts2 = read_knoweledge_base('kb.txt')
print(facts2)

'''The initial defined facts as set'''
print("***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&**\n")
# facts = set(input("\n--------------------------------------- Enter the Intial Defined Facts ---------------------------------------\n").split())


'''While loop until there is no new facts were derived
Perform Forward Chaining'''

def forward(facts,knowledge_base):
    facts = set(facts)
    while True:
        print("1")
        new_facts=set()
        for rule in knowledge_base:
            if set(x in facts for x in rule["antecendts"]) == set([True]):
                new_facts.update(rule["consequent"])
        print(new_facts.difference(facts))
        if not new_facts.difference(facts):
        #     '''Break the loop if there will be no new facts were defined'''
            break
        
        facts.update(new_facts)
    

    return facts
        # new_facts = set()

        # for fact in facts:
        #     if fact in knowledge_base:
        #         new_facts.update(knowledge_base[fact])

        # if not new_facts.difference(facts):
        #     '''Break the loop if there will be no new facts were defined'''
        #     break

        # facts.update(new_facts)
   
    

'''The final list after performing Forward Chaining'''

print("\n***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&***&&&**\n")
print("-------------------------------- Results after performing forward chaining -----------------------------------\n")
# print(facts2,'\n')

re1 = forward(facts2,knowledge_base2)
print(re1)

'''Backward Chaining'''

# knowledge_base1 = {'Q': [['P']], 'P': [['L', 'M']], 'L': [['A', 'P'], ['A', 'B']], 'M': [['B', 'L']], 'A': [], 'B': []}
# print(knowledge_base1)

# def backward_chaining(goal, kb, facts, steps=[]):
#     if goal in facts:
#         steps.append(f"{goal} is already known")
#         return True,steps
#     for rule, result in kb.items():
#         if goal in result:
#             steps.append(f"Using rule: {rule}")
#             new_goals = [k for k in result]
#             for new_goal in new_goals:
#                 tmp,step = backward_chaining(new_goal, kb, facts, steps)
#                 if not tmp:
#                     steps.append(f"{new_goal} cannot be proved")
#                     return False,steps
#             steps.append(f"All sub-goals {new_goals} can be proved using rule {rule}")
#             return True,steps
#     steps.append(f"{goal} cannot be proved")
#     return False,steps


# facts1 = set(input("\n--------------------------------------- Enter the Intial Defined Facts ---------------------------------------\n").split())
# result,step = backward_chaining('Q',knowledge_base1,facts1,steps=[])
# print(step)