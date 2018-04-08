import numpy
def matrixElementsSum(matrix):
    val = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 0):
                matrix[i+1][j]=0
    val = [sum(row) for row in matrix]
    return sum(val)
