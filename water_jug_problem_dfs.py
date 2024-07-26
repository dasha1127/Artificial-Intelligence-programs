def is_valid_state(state, a, b):
    jug1, jug2 = state
    return 0 <= jug1 <= a and 0 <= jug2 <= b

def is_goal_state(state, target):
    jug1, jug2 = state
    return jug1 == target or jug2 == target

def get_successors(state, a, b):
    jug1, jug2 = state
    successors = []

    # Fill Jug1
    successors.append((a, jug2))
    # Fill Jug2
    successors.append((jug1, b))
    # Empty Jug1
    successors.append((0, jug2))
    # Empty Jug2
    successors.append((jug1, 0))
    # Pour Jug1 to Jug2
    pour_to_jug2 = min(jug1, b - jug2)
    successors.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
    # Pour Jug2 to Jug1
    pour_to_jug1 = min(jug2, a - jug1)
    successors.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    return [succ for succ in successors if is_valid_state(succ, a, b)]

def dfs_water_jug(a, b, target):
    stack = [(0, 0)]
    visited = set()
    path = []

    while stack:
        state = stack.pop()
        if state in visited:
            continue

        visited.add(state)
        path.append(state)

        if is_goal_state(state, target):
            return path

        for successor in get_successors(state, a, b):
            if successor not in visited:
                stack.append(successor)

    return None

# Example usage
a = 2 # Capacity of Jug A
b = 2  # Capacity of Jug B
target = 3  # Target amount of water

solution = dfs_water_jug(a, b, target)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
