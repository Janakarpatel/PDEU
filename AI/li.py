

def read_knoweledge_base(filename):
    kb = {}

    with open(filename,'r') as file:
        for line in file:
            rule = line.strip().split('-')

            if len(rule) == 1:
                fact = rule[0].strip()
                consequent = rule[1].strip()
                kb[consequent].append(fact)
            else:
                consequent = rule[1].strip()
                antecedents = rule[0].split('.')
                antecedents = [antecedent.strip() for antecedent in antecedents]
                for ant in antecedents:
                    kb.setdefault(ant,[]).append(consequent)

    return kb

knowledge_base1 = read_knoweledge_base('kb.txt')
print(knowledge_base1)

def backward_chaining(goal, kb, facts, steps=[]):
    if goal not in facts:
        new_goal = []
        new_goal.append(goal)

        for rule in kb:
            lst=kb[rule]
            if goal in lst:
                backward_chaining(rule,kb,facts,steps)
    else:
        facts.append(goal)
        return steps



facts1 = set(["A","B"])
result,step = backward_chaining('Q',knowledge_base1,facts1,steps=[])
print(step)