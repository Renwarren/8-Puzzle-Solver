from time import time
from bfs import BFS
from dfs import DFS
from gbfs import Greedy
from astar import AStar_search

from utils import *

#initial state
print("Enter your puzzle")
root = []
for i in range(0,9):
    p = int(input())
    root.append(p)

print("The given state is:", root)

if isSolvable(root):
    print("Solvable, please wait. \n")
    
    time1 = time()
    BFS_solution = BFS(root, 3)
    BFS_time = time() - time1
    print('BFS Solution is ', BFS_solution[0])
    print('Number of explored nodes is ', BFS_solution[1])    
    print('BFS Time:', BFS_time , "\n")
          
    time2 = time()
    DFS_solution = DFS(root, 3)
    DFS_time = time() - time2
    print('DFS Solution is ', DFS_solution[0])
    print('Number of explored nodes is ', DFS_solution[1])
    print('DFS Time:', DFS_time, "\n")  
    
    time3 = time()
    Greedy_solution = Greedy(root, 3)
    Greedy_time = time() - time3
    print('Greedy Solution is ', Greedy_solution[0])
    print('Number of explored nodes is ', Greedy_solution[1])   
    print('Greedy Time:', Greedy_time , "\n")
    
    time4 = time()
    AStar_solution = AStar_search(root, 3)
    AStar_time = time() - time4
    print('A* Solution is ', AStar_solution[0])
    print('Number of explored nodes is ', AStar_solution[1])   
    print('A* Time:', AStar_time)
    
    
else:
    print("Not solvable")



     