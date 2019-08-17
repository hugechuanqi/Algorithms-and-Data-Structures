## 题目：矩阵中的路径
## 类型：回溯法

## 题目描述：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bccced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

## 输入：矩阵
# a  b  c  e
# s  f   c  s
# a  d  e  e
## 输出：
# True

## 思路：二维矩阵中找路径，通常都可以用回溯法来解决。

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(matrix, rows, cols, path[1:], i, j):
                        return True
        return False
    
    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols + j] = '0'    # 将找过的值赋值为0
        if j+1<cols and matrix[i*cols+j+1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j+1)  # 向右寻找
        elif j-1>=0 and matrix[i*cols+j-1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1)  # 向左寻找
        elif i+1<rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i+1, j)  # 向下寻找
        elif i-1>=0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i-1, j)
        else:
            return False

if __name__ == "__main__":
    # matrix = [["a","b","c","e"],["s","f","c","s"],["a","d","e","e"]]
    matrix = ["a","b","c","e", "s","f","c","s", "a","d","e","e"]
    rows, cols = 3, 4
    path = "bccee"
    a = Solution()
    print(a.hasPath(matrix, rows, cols, path))


