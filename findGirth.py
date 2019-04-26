
m = [[0,1,0,0,1],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

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

    print("WIN")
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

findGirth(m)