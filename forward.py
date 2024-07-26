# Define rules as functions
def rule1(facts):
    if 'fever' in facts and 'cough' in facts:
        return 'flu'
    return None

def rule2(facts):
    if 'fever' in facts and 'sore throat' in facts:
        return 'cold'
    return None

# Forward chaining function
def forward_chaining(facts, rules):
    conclusions = set()
    while True:
        new_conclusions = set()
        for rule in rules:
            result = rule(facts)
            if result and result not in facts:
                new_conclusions.add(result)
                facts.add(result)
        if not new_conclusions:
            break
    return facts

# Initial facts
facts = {'fever', 'cough'}

# List of rules
rules = [rule1, rule2]

# Run forward chaining
results = forward_chaining(facts, rules)
print(f"Diagnosed conditions (Forward Chaining): {results}")
