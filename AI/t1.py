def backward_chaining(goal, rules, facts, path=[]):
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
                antecedent_proven, path = backward_chaining(antecedent, rules, facts, path)
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

# Define the rules and facts
rules = [{'antecendts': ['P'], 'consequent': 'Q'}, {'antecendts': ['L', 'M'], 'consequent': 'P'}, {'antecendts': ['B', 'L'], 'consequent': 'M'}, {'antecendts': ['A', 'B'], 'consequent': 'L'}]

facts = ['A','B']

# Test the function with some goals
goal = "Q"
result, path = backward_chaining(goal, rules, facts)
if result:
    print(f"{goal} can be proven using the following facts and rules:")
    for item in path:
        if type(item) == str:
            print(f"- {item}")
        else:
            print(f"- {' and '.join(item['antecendts'])} => {item['consequent']}")
else:
    print(f"{goal} cannot be proven using the existing facts and rules.")
    
goal = "K"
result, path = backward_chaining(goal, rules, facts)
if result:
    print(f"{goal} can be proven using the following facts and rules:")
    for item in path:
        if type(item) == str:
            print(f"- {item}")
        else:
            print(f"- {' and '.join(item['antecedents'])} => {item['consequent']}")
else:
    print(f"{goal} cannot be proven using the existing facts and rules.")
    
goal = "N"
result, path = backward_chaining(goal, rules, facts)
if result:
    print(f"{goal} can be proven using the following facts and rules:")
    for item in path:
        if type(item) == str:
            print(f"- {item}")
        else:
            print(f"- {' and '.join(item['antecedents'])} => {item['consequent']}")
else:
    print(f"{goal} cannot be proven using the existing facts and rules.")
