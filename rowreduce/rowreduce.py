#   uncomment the line below to enable debug mode
#import pdb; pdb.set_trace()
import math

def GetRow(mat, row):
    #return row from matrix mat
    retVec=[mat[row][j] for j in range(len(mat[0]))]
    return(retVec)

def swapRows(mat, row1, row2):
    #   store second row values first
    temp = GetRow(mat, row2)
    #   then swap
    mat[row2] = GetRow(mat, row1)
    mat[row1] = temp
    
def getBestPartialPivot(mat, pivotCol):
    #   set initial values for the pivot row, and pivot value
    maxPivotValue = mat[pivotCol][pivotCol]
    maxPivotRow = pivotCol
    #   Check the rest of the rows for a higher pivot value
    for i in range(pivotCol + 1, len(mat)):
        if mat[i][pivotCol] > maxPivotValue:
            #   set new max
            maxPivotValue = mat[i][pivotCol]
            maxPivotRow = i
    #   now the new max pivot row can be swapped in, if there is one
    if maxPivotRow != pivotCol:
        swapRows(mat, pivotCol, maxPivotRow)
    
def setBestPivotRow(mat, pivotColIndex, pivotStrategy):
    if pivotStrategy == 0:
        #   no strategy
        return
    if pivotStrategy == 1:
        #   partial pivoting
        getBestPartialPivot(mat, pivotColIndex)
        return
    if pivotStrategy == 2:
        #   scaled pivoting
        return
    
def showMatrix(mat):
    "Print out matrix"
    for row in mat:
        print(row)

#   This function uses a pivot row to remove that pivot value
#   From another row
def removePivotValueFromRow(col, pivotRow, rowToClean):
    pivotRatio = rowToClean[col]
    if pivotRatio != 0:
        for i in range(len(pivotRow)):
            rowToClean[i] -= pivotRow[i] * pivotRatio
    return(rowToClean)
    
#   This function will divide every value in the row by the pivot value
#   The result is that the pivot is changed to 1
def setPivotToOne(col, pivotRow):
    if pivotRow[col] != 0:
        divisor = pivotRow[col]
        for i in range(col, len(pivotRow)):
            pivotRow[i] /= divisor
    return(pivotRow)
       
def solveMatrix(mat, pivotStrategy):
    #    for each row in the matrix
    for i in range(len(mat)):
        #   0: no pivot strategy
        #   1: partial pivot strategy
        #   2: scaled pivot strategy
        setBestPivotRow(mat, i, pivotStrategy)
        #    set pivot in row to 1
        setPivotToOne(i, mat[i])
        #    remove value in pivot column from other rows    
        for j in range(len(mat)):
            if j != i:
                removePivotValueFromRow(i, mat[i], mat[j])
    return(mat)


######  Initial tests

A= [[4,-2,1,11],
    [-2,4,-2,-16],
    [1,-2,4,17]]
    
testMat =  [[1.,1.,1.,6.],
            [0.,2.,5.,-4.],
            [2.,5.,-1.,27.]]
            
testMatDesiredResult = [[1,0,0,5],
                        [0,1,0,3],
                        [0,0,1,-2]]
       
#   Source augmented matrix for homework part 2       
part2Mat =  [[1.000,1.000,1.000,0.001,3.0],
             [1.000,0.001,0.001,0.001,1.0],
             [1.000,1.000,0.001,0.001,2.0],
             [10.00,10.00,10.00,math.pow(10,17),math.pow(10,17)]]
                
def testRowOps():
    print("Matrix")
    showMatrix(testMat)
    print("After row 3 has pivot1 removed")
    testMat[2] = removePivotValueFromRow(0, testMat[0], testMat[2])
    showMatrix(testMat)
    
def testMatrix():
    print("Matrix")
    showMatrix(testMat)
    print("solved matrix")
    showMatrix(solveMatrix(testMat, 1))
    
def testPivotOps():
    print("Matrix for part 2:")
    showMatrix(part2Mat)
    print("row 1 and 3 swapped:")
    swapRows(part2Mat,0,2)
    showMatrix(part2Mat)
    print("get best row for pivot 1 by partial pivoting:")
    setBestPivotRow(part2Mat, 0, 1)
    showMatrix(part2Mat)
    
#testRowOps()
testMatrix()
#testPivotOps()