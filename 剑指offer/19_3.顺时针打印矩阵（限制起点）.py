## 核心：边界+循环结束条件——start, endX, endY；start*2 < row
## 难点：打印过的元素不再打印，因此循环时必须要控制好行列的边界，即开始点和结束点
## 疑问：如果限制起点，似乎有问题，如下，如果从7开始，将不会遍历到矩阵所有点
# 1   2    3   4
# 5   6    7   8
# 9   10 11 12
# 13 14 15 16

class Solution:
    def printMatrix(self, matrix,,startX, startY):
        res = []
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        while(start*2 < row and start*2 < col):
            endX = row  - 1 - start
            endY = col - 1 - start
            for j in range(start, endY+1):
                temp = matrix[start][j]
                res.append(temp)
            if start<=endY:
                for i in range(start+1, endX+1):
                    temp = matrix[i][j]
                    res.append(temp)
            if start<=endX and start<=endY:
                for j in range(endY-1,start-1,-1):
                    temp = matrix[i][j]
                    res.append(temp)               
            if start<=endX and start<=endY:
                for i in range(endX-1, start, -1):
                    temp = matrix[i][j]
                    res.append(temp)
                
            start = start + 1
        return res

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    a = Solution()
    startX, startY = 1,2
    res = a.printMatrix(matrix,startX, startY)
    print(res)


