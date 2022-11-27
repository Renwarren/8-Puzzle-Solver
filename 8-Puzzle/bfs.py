from state import State
from queue import Queue


def BFS(given_state , n):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return