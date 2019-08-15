## 核心：边界+循环结束条件——start, endX, endY；start*2 < row
## 难点：打印过的元素不再打印，因此循环时必须要控制好行列的边界，即开始点和结束点
## 延伸问题：假设起点设定好了，然后顺时针旋转，又该如何控制

class Solution:
    def printMatrix(self, matrix):
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
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]   #输入矩阵
    a = Solution()
    res = a.printMatrix(matrix)
    print(res)


