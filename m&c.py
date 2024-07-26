import heapq

def is_valid_state(state):
    M, C, _ = state
    if M < 0 or C < 0 or M > 3 or C > 3:
        return False
    if (M > 0 and M < C) or (3 - M > 0 and 3 - M < 3 - C):
        return False
    return True

def is_goal_state(state):
    return state == (0, 0, 0)

def get_successors(state):
    M, C, B = state
    successors = []
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    for move in moves:
        if B == 1:
            new_state = (M - move[0], C - move[1], 0)
        else:
            new_state = (M + move[0], C + move[1], 1)
        
        if is_valid_state(new_state):
            successors.append(new_state)
    
    return successors

def heuristic(state):
    M, C, _ = state
    return M + C

def best_first_search():
    initial_state = (3, 3, 1)
    frontier = [(heuristic(initial_state), initial_state)]
    heapq.heapify(frontier)
    visited = set()
    path = []
    parent_map = {}

    while frontier:
        _, current_state = heapq.heappop(frontier)
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        path.append(current_state)

        if is_goal_state(current_state):
            solution_path = []
            while current_state:
                solution_path.append(current_state)
                current_state = parent_map.get(current_state, None)
            solution_path.reverse()
            return solution_path

        for successor in get_successors(current_state):
            if successor not in visited:
                heapq.heappush(frontier, (heuristic(successor), successor))
                parent_map[successor] = current_state

    return None

solution = best_first_search()
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
