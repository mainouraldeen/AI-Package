# Maze Solver - Search Algorithms.

this program solve a 2-D maze using DFS, BFS, UCS and A* (using 2 different heuristics Euclidian and Manhattan). A maze is path typically from start node ‘S’ to Goal node ‘E’
Input: 2D maze represented as a string and Edge Cost (in case of UCS and A*) Output: i. Path: the path to go from Start to End ii. Full Path: the path of all visited nodes. iii. Total Cost (only in UCS and A*)
For Calculating the heuristic value apply the two methods:
1.	Euclidean: Take the square root of the sum of the squares of the differences of the coordinates. o For example, if x = (a, b) and y=(c, d) , the Euclidean distance between x and y is root((a-c)^2+(b+d)^2)
2.	Manhattan: Take the sum of the absolute values of the differences of the coordinates. o For example, if x = (a, b) and y=(c, d) , the Euclidean distance between x and y is |a-c|+|b-d|

