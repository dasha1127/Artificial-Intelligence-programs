class Node:
    def __init__(self, name, heuristic=0, is_and=False):
        self.name = name
        self.heuristic = heuristic
        self.is_and = is_and
        self.children = []
        self.parent = None

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def __repr__(self):
        return f"Node({self.name}, h={self.heuristic}, is_and={self.is_and})"

def ao_star(node):
    def recursive_ao_star(current_node):
        if not current_node.children:
            return current_node.heuristic

        min_cost = float('inf')
        best_path = None

        if current_node.is_and:
            cost = 0
            for child in current_node.children:
                cost += recursive_ao_star(child)
            cost += current_node.heuristic
            min_cost = cost
            best_path = current_node.children
        else:
            for child in current_node.children:
                cost = recursive_ao_star(child)
                cost += current_node.heuristic
                if cost < min_cost:
                    min_cost = cost
                    best_path = child

        current_node.heuristic = min_cost
        return min_cost

    return recursive_ao_star(node)

# Example usage:

# Creating the nodes
A = Node('A', heuristic=10)
B = Node('B', heuristic=5)
C = Node('C', heuristic=12)
D = Node('D', heuristic=6)
E = Node('E', heuristic=4, is_and=True)

# Setting up the tree
A.add_child(B)
A.add_child(C)
B.add_child(D)
E.add_child(D)
E.add_child(C)
A.add_child(E)

# Running AO* search
result = ao_star(A)
print(f"The heuristic value of the best path is: {result}")
