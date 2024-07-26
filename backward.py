# Define rules as functions
def rule1(facts):
    if 'fever' in facts and 'cough' in facts:
        return 'flu'
    return None

def rule2(facts):
    if 'fever' in facts and 'sore throat' in facts:
        return 'cold'
    return None

# Backward chaining function
def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True
    for rule in rules:
        result = rule(facts)
        if result == goal:
            return True
        if result and backward_chaining(result, facts, rules):
            return True
    return False

# Goal to determine
goal = 'flu'

# Initial facts
facts = {'fever', 'cough'}

# List of rules
rules = [rule1, rule2]

# Run backward chaining
is_goal_achieved = backward_chaining(goal, facts, rules)
print(f"Can achieve goal '{goal}' (Backward Chaining): {is_goal_achieved}")
