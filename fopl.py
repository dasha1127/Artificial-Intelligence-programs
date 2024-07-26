def resolve(clause1, clause2):
    """Resolve two clauses."""
    resolvents = []
    for literal1 in clause1:
        if -literal1 in clause2:
            resolvent = (clause1 - {literal1}) | (clause2 - {-literal1})
            if not resolvent:  # Empty resolvent means contradiction
                return set()
            resolvents.append(resolvent)
    return resolvents

def apply_resolution(kb, goal):
    """Apply resolution to a knowledge base to prove the goal."""
    clauses = set(kb)
    goal_clause = {-goal}
    clauses.add(frozenset(goal_clause))
    
    new_clauses = set()
    while True:
        for clause1 in clauses:
            for clause2 in clauses:
                if clause1 != clause2:
                    resolvents = resolve(clause1, clause2)
                    if not resolvents:
                        return True  # Contradiction found
                    new_clauses.update(resolvents)
        
        if new_clauses.issubset(clauses):
            return False  # No new clauses, goal not provable
        
        clauses.update(new_clauses)

def main():
    # Define knowledge base in CNF format
    kb = [
        frozenset([-1, 2]),  # ¬P(x) ∨ Q(x)
        frozenset([-2, 3])   # ¬Q(a) ∨ R
    ]
    
    # Define goal
    goal = 3  # R
    
    # Apply resolution
    result = apply_resolution(kb, goal)
    if result:
        print("The goal is provable.")
    else:
        print("The goal is not provable.")

if __name__ == "__main__":
    main()
