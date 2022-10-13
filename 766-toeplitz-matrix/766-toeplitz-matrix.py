def topleft(matrix, i , j):
    if i == 0 or j ==0:
        print("i or j is zero")
        return True
    elif matrix[i-1][j-1] == matrix[i][j]:
        return True
    else:
        return False
        
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        res = True
        height = len(matrix) 
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                print(topleft(matrix, i,j))
                res = res and ( topleft(matrix, i,j))
        return res