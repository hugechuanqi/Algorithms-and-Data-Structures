## 题目：矩阵相邻搜索
## 类型：矩阵，回溯法
## 应用：涉及到机器人行走路径

## 题目描述：给定一个矩阵，然后给你一个路径，matrix=[[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45]]，path=[1,2,3,4,5,11]，并且矩阵中的路径可以超出限制，判断是否存在所给定路径
## 核心：1、如何找到第一个路径点；2、如何沿着这条路径依次行走，包括向上、向下、向左、向右，每次都得判断是否超出边界；3此题似乎可以超出边界。
## 思路：首先输入一个矩阵和路径，首先？？？
# python知识扩展：对于if j+1<cols and matrix[i][j+1] == path[0]:，首先判断第一个条件j+1<cols是否满足，如果不满足则第二个条件不会执行，满足才会执行。


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """ 找到起点，并开始行走
        """
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    if self.find2(matrix, rows, cols, path[1:], i, j):
                        return True
        return False
    
    def find(self, matrix, rows, cols, path, i, j):
        """ 开始递归判断上下左右哪个路径符合行走路径
        """
        if not path:
            return True
        matrix[i][ j] = '0'    # 将找过的值赋值为0
        # print(i, j, path, rows, matrix[i+1][j])
        if j+1<cols and matrix[i][j+1] == path[0]:
            print(matrix[i][j+1], matrix)
            return self.find(matrix, rows, cols, path[1:], i, j+1)  # 向右寻找
        elif j-1>=0 and matrix[i][j-1] == path[0]:
            print(matrix[i][j-1], matrix)
            return self.find(matrix, rows, cols, path[1:], i, j-1)  # 向左寻找
        elif i+1<rows and matrix[i+1][j] == path[0]:
            print(matrix[i+1][j], matrix)
            return self.find(matrix, rows, cols, path[1:], i+1, j)  # 向下寻找
        elif i-1>=0 and matrix[i-1][j] == path[0]:
            print(matrix[i-1][j], matrix)
            return self.find(matrix, rows, cols, path[1:], i-1, j)  # 向上寻找
        else:
            return False

    def find2(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i][ j] = '0'    # 将找过的值赋值为0
        print(i, j, path, rows, cols, matrix[i+1][j], j+1==cols)
        if j+1<cols and matrix[i][j+1] == path[0]:
            print(matrix[i][j+1], matrix)
            return self.find2(matrix, rows, cols, path[1:], i, j+1)  # 向右寻找
        elif j-1>=0 and matrix[i][j-1] == path[0]:
            print(matrix[i][j-1], matrix)
            return self.find2(matrix, rows, cols, path[1:], i, j-1)  # 向左寻找
        elif i+1<rows and matrix[i+1][j] == path[0]:
            print(matrix[i+1][j], matrix)
            return self.find2(matrix, rows, cols, path[1:], i+1, j)  # 向下寻找
        elif i-1>=0 and matrix[i-1][j] == path[0]:
            print(matrix[i-1][j], matrix)
            return self.find2(matrix, rows, cols, path[1:], i-1, j)  # 向上寻找

        elif i-1 == -1 and 0<=j<=cols-1:     # 超出上边边界
            print("ok")
            i = rows-1
            if j+1<cols and matrix[i][(cols+ j+1)//cols] == path[0]:
                print(matrix[i][j+1], matrix)
                return self.find2(matrix, rows, cols, path[1:], i,(cols+ j+1)//cols)  # 向右寻找
            elif j-1>=0 and matrix[i][(cols+j-1)//cols] == path[0]:
                print(matrix[i][j-1], matrix)
                return self.find2(matrix, rows, cols, path[1:], i, (cols+j-1)//cols)  # 向左寻找  

        elif i+1 == rows and 0<=j<=cols-1:   # 超出下边边界
            i = 0
            if matrix[i][(cols+j+1)//cols] == path[0]:
                print(matrix[i][(cols+j+1)//cols], matrix)
                return self.find2(matrix, rows, cols, path[1:], i, (cols+ j+1)//cols)  # 向右寻找
            elif matrix[i][(cols+j-1)//cols] == path[0]:
                print(matrix[i][(cols+j-1)//cols], matrix)
                return self.find2(matrix, rows, cols, path[1:], i, (cols+j-1)//cols)  # 向左寻找

        elif j-1 == -1 and 0<=i<=rows-1:     # 超出左边边界
            j = cols-1
            if i+1<rows and matrix[(rows+i+1)][j] == path[0]:
                print(matrix[(rows+i+1)][j], matrix)
                return self.find2(matrix, rows, cols, path[1:], (rows+i+1)//rows, j)  # 向下寻找
            elif i-1>=0 and matrix[(rows+i-1)//rows][j] == path[0]:
                print(matrix[(rows+i-1)//rows][j], matrix)
                return self.find2(matrix, rows, cols, path[1:], (rows+i-1)//rows, j)  # 向上寻找

        elif j+1 == cols and 0<=i<=rows-1:   # 超出右边边界
            print("ok")
            j = 0
            print(i,j, matrix[ (rows+i+1)//rows][j])
            if i+1<rows and matrix[ (rows+i+1)//rows][j] == path[0]:
                print(matrix[i+1][j], matrix)
                return self.find2(matrix, rows, cols, path[1:], (rows+i+1)//rows, tmp)  # 向下寻找
            elif i-1>=0 and matrix[ (rows+i+1)//rows][j] == path[0]:
                print(matrix[i-1][j], matrix)
                return self.find2(matrix, rows, cols, path[1:], (rows+i-1)//rows, j)  # 向上寻找

        else:
            return False


import sys 
if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45]]
    rows, cols = 5,5
    # for line in sys.stdin:
    #     path = line.split()
    path = [1,2,3,4,5,11]
    a = Solution()
    if a.hasPath(matrix, rows, cols, path):
        print('1')
    else:
        print('0')

## 测试用例：
# [5,15,25,35,45,1]
# [1,2,3,4,5,11]
