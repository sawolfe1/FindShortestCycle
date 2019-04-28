import math
import json

#m = [[0,1,0,0,1],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

m = [
    [0,0,1,1,0,1,0],
    [0,0,1,0,0,0,0],
    [1,1,0,1,0,0,0],
    [1,0,1,0,0,0,0],
    [0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1],
    [0,0,0,0,1,1,0]
    ]

def findGirth(matrix):

    if not checkSquareMatrix(matrix):
        print("Not A Square Matrix")
        return

    if not checkBitValueEntries(matrix):
        print("Not All Entries are Bits")
        return
        
    if not checkSelfLoops(matrix):
        print("Self Loop Detected")
        return

    if not checkSymmetric(matrix):
        print("Not Symmetric")
        return

    print(f"Girth: {girth(matrix)}")
    return

def checkSquareMatrix(matrix):

    length = len(matrix)

    for i in range(length):
        if len(matrix[i]) != length:
            return False

    return True

def checkBitValueEntries(matrix):

    length = len(matrix)

    for i in range(length):
        for j in range(length):
            if ((matrix[i][j] != 1) and (matrix[i][j] != 0)):
                return False

    return True

def checkSelfLoops(matrix):

    length = len(matrix)

    for i in range(length):
        if matrix[i][i] != 0:
            return False
    return True
    
def checkSymmetric(matrix):

    length = len(matrix)
    counter = 0

    for i in range(length):
        for j in range(length):
            counter += matrix[i][j]

    return not counter%2

def girth(matrix):
    length = len(matrix)
    girth = math.inf
    graph = {}
    shortestCycle = "None"
    
    for v in range(length):
        graph[v] = {}
        graph[v]["id"] = v
        graph[v]["color"] = "WHITE"
        graph[v]["d"] = 0
        graph[v]["parent"] = None

    graph[0]["color"] = "GRAY"
    graph[0]["d"] = 0
    graph[0]["parent"] = None
    Q = []
    Q.append(graph[0])
    q = len(Q)
    while q != 0:
        u = Q.pop(0)
        q = len(Q)
        for j in range(length):
            edge = matrix[u["id"]][j]
            if edge:
                print(graph[j]["color"])
                if graph[j]["color"] == "WHITE":
                    graph[j]["color"] = "GRAY"
                    graph[j]["d"] = u["d"] + 1
                    graph[j]["parent"] = u
                    Q.append(graph[j])
                    q = len(Q)
                elif graph[j]["color"] == "GRAY" and graph[u['id']]['parent']['id'] != graph[j]['id']:
                    cycleLength = graph[u["id"]]["d"] + graph[j]["d"] + 1
                    if cycleLength < girth :
                        girth = cycleLength
                        shortestCycle = f"{graph[u['id']]['id']} --> {graph[j]['id']} --> {graph[j]['parent']['id']} --> "
                        parent = graph[j]["parent"]
                        for k in range(girth-2):
                            if parent['parent'] != None:
                                shortestCycle += f"{parent['parent']['id']} --> "
                        shortestCycle += f"{graph[u['id']]['id']}"


        u["color"] = "BLACK"

    print(json.dumps(graph, indent = 2))
    print(f"Shortest Cycle: {shortestCycle}")
    return(girth)

findGirth(m)