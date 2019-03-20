### 题目描述：
### 给定一个矩阵m，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，返回所     有路径中最小的路径和。

# 解法一：将矩阵当作一个二维矩阵（list存储），做双层循环
class Solution:
    def getMaxValue(self, arr, rows, cols):
        if len(arr)==0 or rows<=0 or cols<=0:
            return 0
        maxValue = [[0]*rows]*cols   #建立一个空的二维数组
        for i in range(rows):
            for j in range(cols):
                up = 0
                left = 0
                #到达坐标(i,j)的格子时，能够拿到的礼物最大价值依赖于坐标为(i-1,j)和(i,j-1)的两个格子
                if i>0:
                    up = maxValue[i-1][j]
                if j>0:
                    left = maxValue[i][j-1]
                
                maxValue[i][j] = max(up,left) + arr[i][j]
        
        value = maxValue[rows-1][cols-1]

        return value

a = Solution()
s = [[1,10,3,8], [12,2,9,5], [5,7,4,11], [3,7,16,5]]
rows = len(s[0])
cols = len(s)
print("初始礼物矩阵为：")
for i in range(rows):
    print(s[i])

print("矩阵中从左上角到右下角的最大礼物价值为：",a.getMaxValue(s,rows,cols))

## 解法二：将矩阵当作一维数组（即共rows*cols个元素，list存储），也作双层循环
# class Solution:
#     def getmaxValue(self, values, rows, cols):
#         if not values or rows<=0 or cols <=0:
#             return 0
#         # 用于存放中间数值的临时数组
#         temp = [0] * cols

#         for i in range(rows):
#             for j in range(cols):
#                 left = 0
#                 up = 0

#                 if i > 0:
#                     up = temp[j]
#                 if j > 0:
#                     left = temp[j-1]
#                 temp[j] = max(up,left) + values[i*rows+j]
#         return temp[-1]
# s = Solution()
# a = s.getmaxValue([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4)

