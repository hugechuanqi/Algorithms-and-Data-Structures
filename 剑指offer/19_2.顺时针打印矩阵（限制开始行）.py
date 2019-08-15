## 核心：边界+循环结束条件——start, endX, endY；start*2 < row
## 难点：打印过的元素不再打印，因此循环时必须要控制好行列的边界，即开始点和结束点。此时的开始行数有限制
## 扩展：限制开始列、结束列、结束行都是同样的原理，只需要在循环时控制好开始点和结束点即可，但是边界不变

class Solution:
    def printMatrix(self, matrix, start_row):
        res = []
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        while(start*2 < row-start_row and start*2 < col):
            endX = row  - 1 - start
            endY = col - 1 - start
            for j in range(start, endY+1):
                temp = matrix[start+start_row][j]
                res.append(temp)
            if start<=endY:
                for i in range(start+start_row+1, endX+1):
                    temp = matrix[i][j]
                    res.append(temp)
            if start<=endX and start<=endY:
                for j in range(endY-1,start-1,-1):
                    temp = matrix[i][j]
                    res.append(temp)               
            if start<=endX and start<=endY:
                for i in range(endX-1, start+start_row, -1):
                    temp = matrix[i][j]
                    res.append(temp)
                
            start = start + 1
        return res

if __name__ == "__main__":
    matrix = [[1,3,4],[8,8,7],[5,9,10],[1,3,4]]     #输入矩阵
    a = Solution()
    restricRow = 2
    res = a.printMatrix(matrix, restricRow-1)
    print(res)


