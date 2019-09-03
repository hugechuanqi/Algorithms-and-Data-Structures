class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(matrix, rows, cols, path[1:], i, j, path[0]):
                        return True
        return False
    
    def find(self, matrix, rows, cols, path, i, j, key):
        if not path:
            return True
        matrix[i*cols + j] = '0'    # 将找过的值赋值为0

        if j+1<cols and matrix[i*cols+j+1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j+1, key)  # 向右寻找
        elif j+1<cols and matrix[i*cols+j+1] == key:
            return self.find(matrix, rows, cols, path, i, j+1, key)  # 向右寻找

        elif j-1>=0 and matrix[i*cols+j-1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1, key)  # 向左寻找
        elif j-1>=0 and matrix[i*cols+j-1] == key:
            return self.find(matrix, rows, cols, path, i, j-1, key)  # 向左寻找

        elif i+1<rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i+1, j, key)  # 向下寻找
        elif i+1<rows and matrix[(i+1)*cols+j] == key:
            return self.find(matrix, rows, cols, path, i+1, j, key)  # 向下寻找

        elif i-1>=0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i-1, j, key)  # 向上寻找
        elif i-1>=0 and matrix[(i-1)*cols+j] == key:
            return self.find(matrix, rows, cols, path, i-1, j, key)  # 向上寻找

        else:
            return False

if __name__ == "__main__":
    # matrix = [["a","b","c","e"],["s","f","c","s"],["a","d","e","e"]]
    matrix = ["a","b","c","e", "s","f","c","s", "a","d","e","e"]
    rows, cols = 3, 4
    path = "bccee"
    a = Solution()
    print(a.hasPath(matrix, rows, cols, path))


    # num1 = [5, 10, 15]
    # num2 = [i**2 if i ==10 else i-5 if i<7 else i+5 for i in num1]
    # num2 = []
    # for i in num1:
    #     if i==10:
    #         num2.append(i**2)
    #     else:
    #         if i<7:
    #             num2.append(i-5)
    #         else:
    #             num2.append(i+5)

    # print(num2)