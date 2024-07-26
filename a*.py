class Node:
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos


def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list = [start_node]
    closed_list = []

    while open_list:
        current_node = open_list[0]
        current_index = 0
        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = i

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        children = []
        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_pos = (current_node.pos[0] + new_pos[0], current_node.pos[1] + new_pos[1])
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[0]) - 1) or node_pos[1] < 0:
                continue
            if maze[node_pos[0]][node_pos[1]] != 0:
                continue
            new_node = Node(current_node, node_pos)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue
            child.g = current_node.g + 1
            child.h = ((child.pos[0] - end_node.pos[0]) ** 2) + ((child.pos[1] - end_node.pos[1]) ** 2)
            child.f = child.g + child.h

            if any(open_node for open_node in open_list if child == open_node and child.g > open_node.g):
                continue

            open_list.append(child)


def main():
    maze = [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 6)
    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
