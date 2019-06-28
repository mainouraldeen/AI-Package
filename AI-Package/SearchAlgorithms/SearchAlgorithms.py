import re
import math
import sys
import heapq
import collections
import queue


##############################################################################################################
class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = sys.maxsize  # Represents the cost on the edge from ancurrentY parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    fOfN = sys.maxsize
    heuristicFn = None  # Represents the value of heuristic function
    xCoordinate = None
    yCoordinate = None

    def __init__(self, value):
        self.value = value


# numOfRows = 0
# numOfCols = 0


##############################################################################################################
class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes currentYou need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    startNodeID = 0
    costsList = []

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        self.path.clear()
        self.fullPath.clear()

        self.maze = list(re.split(" ", mazeStr))  # split rows
        newList = []  # list of list rows+ cols splitted
        _2dList = []

        for rowElement in self.maze:  # split cols
            newList = re.split(",", rowElement)
            _2dList.append(newList)

        self.maze = _2dList

        self.numOfRows = _2dList.__len__()
        self.numOfCols = _2dList[0].__len__()

        rowIndex = 0
        colIndex = 0
        id = 0

        # the main loop for filling maze data and converting elements to nodes
        for rowElement in self.maze:
            colIndex = 0
            for value in rowElement:
                newNode = Node(value)

                newNode.id = id

                if edgeCost != None:
                    self.costsList = edgeCost

                newNode.right = newNode.id + 1
                newNode.left = newNode.id - 1
                newNode.down = newNode.id + self.numOfCols
                newNode.up = newNode.id - self.numOfCols
                newNode.xCoordinate = int(id / self.numOfCols)
                newNode.yCoordinate = int(id % self.numOfCols)

                # special conditions
                if newNode.id < self.numOfCols:  # first row
                    newNode.up = None
                # elif numOfRows - rowPosition <= 1:  # last row
                elif newNode.id > ((self.numOfRows * self.numOfCols) - self.numOfCols) - 1:  # last row
                    newNode.down = None

                if not (newNode.id % self.numOfCols):  # first col
                    newNode.left = None
                elif not ((newNode.id + 1) % self.numOfCols):  # last col
                    newNode.right = None

                self.maze[rowIndex][colIndex] = newNode
                if value == "S":
                    self.startNodePosition = (rowIndex, colIndex) #save the position of start node in a tuple
                    self.startNodeID = id
                    self.maze[rowIndex][colIndex].gOfN = 0

                elif value == "E":
                    self.goalNodePosition = (rowIndex, colIndex) #save the position of goal node in a tuple
                    newNode.xCoordinate = int(id / self.numOfCols)
                    newNode.yCoordinate = int(id % self.numOfCols)
                    self.maze[rowIndex][colIndex].hOfN = 0

                colIndex += 1
                id += 1
            rowIndex += 1

    #######################################################################################################
    #takes the id of the node and returns the node itself
    def getCoordinates(self, nodeId):
        for i in range(self.numOfRows):
            for j in range(self.numOfCols):
                if self.maze[i][j].id == nodeId:
                    return self.maze[i][j]

    ######################################################################################################
    def DFS(self):
        self.fullPath.clear()
        self.maze[self.startNodePosition[0]][
            self.startNodePosition[1]].previousNode = None  # setting start node's parent to none

        visitedNodes = []
        openedNodes = []
        openedNodes.insert(0, self.maze[self.startNodePosition[0]][self.startNodePosition[1]])

        while openedNodes.__len__():
            currentNode = openedNodes[0]  # first element in queue

            openedNodes.pop(0)
            visitedNodes.append(currentNode)

            if currentNode.value == "E":
                break

            # adding all neighbours
            if currentNode.right != None:
                childNode = self.getCoordinates(currentNode.right)

                if childNode.value != "#" and childNode not in visitedNodes and childNode not in openedNodes:

                    openedNodes.insert(0, childNode)

                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

            if currentNode.left != None:
                childNode = self.getCoordinates(currentNode.left)
                if childNode.value != "#" and childNode not in visitedNodes and (childNode not in openedNodes):
                    openedNodes.insert(0, childNode)

                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

            if currentNode.down != None:
                childNode = self.getCoordinates(currentNode.down)
                if childNode.value != "#" and childNode not in visitedNodes and (childNode not in openedNodes):
                    openedNodes.insert(0, childNode)

                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

            if currentNode.up != None:
                childNode = self.getCoordinates(currentNode.up)
                if childNode.value != "#" and childNode not in visitedNodes and (childNode not in openedNodes):
                    openedNodes.insert(0, childNode)
                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

        for n in visitedNodes:
            self.fullPath.append(n.id)

        return [], self.fullPath

    ######################################################################################################
    def BFS(self):

        self.fullPath.clear()
        self.maze[self.startNodePosition[0]][
            self.startNodePosition[1]].previousNode = None  # setting start node's parent to none

        visitedNodes = []
        openedNodes = []
        openedNodes.append(self.maze[self.startNodePosition[0]][self.startNodePosition[1]])

        while openedNodes.__len__():
            currentNode = openedNodes[0]  # first element in queue

            openedNodes.pop(0)
            visitedNodes.append(currentNode)
            # print("current id", currentNode.id)

            if currentNode.value == "E":
                break

            # adding all neighbours
            if currentNode.up != None:
                childNode = self.getCoordinates(currentNode.up)
                if childNode.value != "#" and childNode not in visitedNodes and (childNode not in openedNodes):
                    openedNodes.append(childNode)
                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

            if currentNode.down != None:
                childNode = self.getCoordinates(currentNode.down)
                if childNode.value != "#" and childNode not in visitedNodes and (childNode not in openedNodes):
                    openedNodes.append(childNode)

                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

            if currentNode.left != None:
                childNode = self.getCoordinates(currentNode.left)
                if childNode.value != "#" and childNode not in visitedNodes and (childNode not in openedNodes):
                    openedNodes.append(childNode)

                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

            if currentNode.right != None:
                childNode = self.getCoordinates(currentNode.right)

                if childNode.value != "#" and childNode not in visitedNodes and childNode not in openedNodes:

                    openedNodes.append(childNode)

                    if childNode.previousNode == None:
                        childNode.previousNode = currentNode.id

        for n in visitedNodes:
            self.fullPath.append(n.id)

        return [], self.fullPath

    ######################################################################################################
    def UCS(self):

        self.fullPath.clear()
        self.maze[self.startNodePosition[0]][
            self.startNodePosition[1]].previousNode = None  # setting start node's parent to none

        visitedNodes = []
        openedNodesTuple = []
        openNodes = []
      #  index = 0
                                #cost
        openedNodesTuple.append((self.maze[self.startNodePosition[0]][self.startNodePosition[1]].edgeCost,
                                 #node
                            self.maze[self.startNodePosition[0]][self.startNodePosition[1]]))

        openNodes.append(self.maze[self.startNodePosition[0]][self.startNodePosition[1]])

        self.maze[self.startNodePosition[0]][self.startNodePosition[1]].edgeCost = self.costsList[self.startNodeID]

        while openedNodesTuple.__len__():
            currentCostNode = openedNodesTuple[0]  # first tuple in list

            openedNodesTuple.pop(0)
            visitedNodes.append(currentCostNode[1])#add the node itself
            if currentCostNode[1].value == "E":
                break

            # adding all neighbours
            if currentCostNode[1].up != None:
                childNode = self.getCoordinates(currentCostNode[1].up)
                if childNode.value != "#":
                    if childNode not in visitedNodes:
                        newCost = self.costsList[childNode.id] + currentCostNode[1].edgeCost
                        if newCost <= childNode.edgeCost:
                            childNode.edgeCost = newCost
                            childNode.previousNode = currentCostNode[1].id

                        if childNode not in openNodes:
                            openedNodesTuple.append((newCost, childNode))
                            openNodes.append(childNode)
                        else:
                            #edit el openNodesTuple
                            for i in range(openedNodesTuple.__len__()):
                                if openedNodesTuple[i][1] == childNode:
                                    openedNodesTuple.pop(i)
                                    openedNodesTuple.append((childNode.edgeCost, childNode))
                                    break

            if currentCostNode[1].down != None:
                childNode = self.getCoordinates(currentCostNode[1].down)
                if childNode.value != "#":
                    if childNode not in visitedNodes:
                        newCost = self.costsList[childNode.id] + currentCostNode[1].edgeCost
                        if newCost <= childNode.edgeCost:
                            childNode.edgeCost = newCost
                            childNode.previousNode = currentCostNode[1].id

                        if childNode not in openNodes:
                            openedNodesTuple.append((newCost, childNode))
                            openNodes.append(childNode)
                        else:
                            #edit el openNodesTuple
                            for i in range(openedNodesTuple.__len__()):
                                if openedNodesTuple[i][1] == childNode:
                                    #i[0] = childNode.edgeCost
                                    openedNodesTuple.pop(i)
                                    openedNodesTuple.append((childNode.edgeCost, childNode))
                                    break

            if currentCostNode[1].left != None:
                childNode = self.getCoordinates(currentCostNode[1].left)
                if childNode.value != "#":
                    if childNode not in visitedNodes:
                        newCost = self.costsList[childNode.id] + currentCostNode[1].edgeCost
                        if newCost <= childNode.edgeCost:
                            childNode.edgeCost = newCost
                            childNode.previousNode = currentCostNode[1].id

                        if childNode not in openNodes:
                            openedNodesTuple.append((newCost, childNode))
                            openNodes.append(childNode)
                        else:
                            #edit el openNodesTuple
                            for i in range(openedNodesTuple.__len__()):
                                if openedNodesTuple[i][1] == childNode:
                                    # i[0] = childNode.edgeCost
                                    openedNodesTuple.pop(i)
                                    openedNodesTuple.append((childNode.edgeCost, childNode))
                                    break

            if currentCostNode[1].right != None:
                childNode = self.getCoordinates(currentCostNode[1].right)
                if childNode.value != "#":
                    if childNode not in visitedNodes:
                        newCost = self.costsList[childNode.id] + currentCostNode[1].edgeCost
                        if newCost <= childNode.edgeCost:
                            childNode.edgeCost = newCost
                            childNode.previousNode = currentCostNode[1].id

                        if childNode not in openNodes:
                            openedNodesTuple.append((newCost, childNode))
                            openNodes.append(childNode)
                        else:
                            #edit el openNodesTuple
                            for i in range(openedNodesTuple.__len__()):
                                if openedNodesTuple[i][1] == childNode:
                                    openedNodesTuple.pop(i)
                                    openedNodesTuple.append((childNode.edgeCost, childNode))
                                    break

                    # b sort 3la 7sb el fOfN ely heia awel value f-el pair
            openedNodesTuple = sorted(openedNodesTuple, key=lambda x: x[0])

        for n in visitedNodes:
            self.fullPath.append(n.id)

        #total cost = the cost at the goal node
        self.totalCost = self.maze[self.goalNodePosition[0]][self.goalNodePosition[1]].edgeCost
        return [], self.fullPath, self.totalCost

    ######################################################################################################
    def AStarEuclideanHeuristic(self):
        #set edge cost for each node
        index = 0
        for i in range(self.numOfRows):
            for j in range(self.numOfCols):
                self.maze[i][j].edgeCost = self.costsList[index]
                index +=1


        openList = []
        visitedList = []
        # b7sb el hOfn l-kol node
        for row in self.maze:
            for node in row:
                node.hOfN = math.sqrt(math.pow((node.xCoordinate - self.goalNodePosition[0]), 2) + math.pow(
                    node.yCoordinate - self.goalNodePosition[1], 2))

        self.getCoordinates(self.startNodeID).fOfN = self.getCoordinates(self.startNodeID).hOfN

        openList.append((self.getCoordinates(self.startNodeID).fOfN, self.getCoordinates(self.startNodeID)))

        # b7sb el gOfN w el fOfN
        # for nodeFOfN, node in openList:  # el node el hia el parent ll right w ll left w ll up w ll down
        while openList.__len__():

            node = openList[0][1]
            # nodeFOfN = openList[0][0]
            if node.value == "E":
                visitedList.append(node)
                break
            openList.pop(0)
            if node not in visitedList:
                visitedList.append(node)
            else:
                continue

            if node.up != None:
                childNode = self.getCoordinates(node.up)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = childNode.edgeCost + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + childNode.edgeCost + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + childNode.edgeCost + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            if node.down != None:
                childNode = self.getCoordinates(node.down)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = childNode.edgeCost + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + childNode.edgeCost + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + childNode.edgeCost + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            if node.left != None:
                childNode = self.getCoordinates(node.left)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = childNode.edgeCost + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + childNode.edgeCost + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + childNode.edgeCost + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            if node.right != None:
                childNode = self.getCoordinates(node.right)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = childNode.edgeCost + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + childNode.edgeCost + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + childNode.edgeCost + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            # b sort 3la 7sb el fOfN ely heia awel value f-el pair
            openList = sorted((fofn, n) for fofn, n in openList)

        for n in visitedList:
            self.fullPath.append(n.id)

        self.totalCost = self.maze[self.goalNodePosition[0]][self.goalNodePosition[1]].fOfN

        return [], self.fullPath, self.totalCost

    ######################################################################################################
    def AStarManhattanHeuristic(self):
        self.fullPath.clear()
        openList = []
        visitedList = []

        # setting heuristic value for each node
        for row in self.maze:
            for node in row:
                node.hOfN = abs(node.xCoordinate - self.goalNodePosition[0]) + abs(
                    node.yCoordinate - self.goalNodePosition[1])

        # hofn = fofn for first node and gofn =0
        self.getCoordinates(self.startNodeID).fOfN = self.getCoordinates(self.startNodeID).hOfN

        # add start node in open list as pair (fofn and id)
        openList.append((self.getCoordinates(self.startNodeID).fOfN, self.getCoordinates(self.startNodeID)))

        # b7sb el gOfN w el fOfN
        # for nodeFOfN, node in openList:  # el node el hia el parent ll right w ll left w ll up w ll down
        while openList.__len__():

            node = openList[0][1]
            # nodeFOfN = openList[0][0]
            if node.value == "E":
                visitedList.append(node)
                break
            openList.pop(0)
            if node not in visitedList:
                visitedList.append(node)
            else:
                continue

            if node.up != None:
                childNode = self.getCoordinates(node.up)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = 1 + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + 1 + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + 1 + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            if node.down != None:
                childNode = self.getCoordinates(node.down)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = 1 + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + 1 + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + 1 + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            if node.left != None:
                childNode = self.getCoordinates(node.left)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = 1 + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + 1 + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + 1 + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN

            if node.right != None:
                childNode = self.getCoordinates(node.right)
                if childNode.value != "#":
                    if childNode not in visitedList:
                        childNode.gOfN = 1 + node.gOfN

                    # bshof el f(N) el gedida w el f(N) bta3ty men el as8r
                    if node.gOfN + 1 + childNode.hOfN < childNode.fOfN:
                        childNode.fOfN = node.gOfN + 1 + childNode.hOfN
                        childNode.previousNode = node.id

                    if childNode not in openList:
                        openList.append((childNode.fOfN, childNode))
                    else:
                        # law el child magod fel open list bs el fOfN bta3to et8airt
                        # hadwer 3alih f-el openList w a-update el fOfN bta3to
                        for i in openList:
                            if i[1] == childNode:
                                i[0] = childNode.fOfN


            # b sort 3la 7sb el fOfN ely heia awel value f-el pair
            openList = sorted(openList, key=lambda x: x[0])

        for n in visitedList:
            self.fullPath.append(n.id)

        self.totalCost = float(self.maze[self.goalNodePosition[0]][self.goalNodePosition[1]].fOfN)
        return [], self.fullPath, self.totalCost


######################################################################################################

def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
