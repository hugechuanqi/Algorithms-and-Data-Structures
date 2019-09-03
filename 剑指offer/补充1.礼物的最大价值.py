## 题目：礼物的最大价值
## 类型：动态规划

## 题目描述：在一个m*n的棋盘的每一个格都放有一个礼物，每个礼物都有一定价值（大于0）。从左上角开始拿礼物，每次向右或向下移动一格，直到右下角结束。给定一个棋盘，求拿到礼物的最大价值。例如，对于如下棋盘
## 输入：
# 1   10  3   8
# 12  2   9   6
# 5    7   4  11
# 3    7 16   5
## 输出：
# 53 = 1+12+5+7+7+16+5

## 核心：构造动态规划矩阵，从矩阵最小的位置，根据规则的变化（向下或向上移动），直到矩阵最后的位置。
## 思路：给定一个动态规划矩阵dp[N][M]，从左上角开始每次只能向右或者向下走，每次判断向左和向右的较大值，较大值的方向就是棋子行走的方向，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，返回所有路径中最大的路径和。


class Solution:
    def getMaxValue(self, Arr, rows, cols):
        """ 记忆化搜索：构造二维动态规划矩阵，需要双层循环，每次都将
        """
        if len(Arr)==0 or rows<=0 or cols<=0:
            return 0
        maxValue = [[0]*rows]*cols   #建立一个空的二维数组  # maxValue = [[0 for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                up, left = 0, 0
                if i>0:
                    up = maxValue[i-1][j]   # 记录向下走的代价
                if j>0:
                    left = maxValue[i][j-1] # 记录向右走的代价
                maxValue[i][j] = max(up,left) + Arr[i][j]   # 判断之前的行走路径中，哪个更大，将礼物值更大与当前礼物值相加，构成礼物总值
        
        value = maxValue[rows-1][cols-1]
        return value

    def getMaxValue2(self, Arr, rows, cols):
        """ 动态规划：构造二维动态规划矩阵，需要双层循环——可能会超出内存
        """
        if len(Arr)==0 or rows<=0 or cols<=0:
            return 0
        maxValue = [[0 for j in range(cols)] for i in range(rows)]
        maxValue[0][0] = Arr[0][0]
        for i in range(1,rows):     # 首先计算出动态规划值的第一列，即一直向下走
            maxValue[i][0] = maxValue[i-1][0]+Arr[i][0]
        for j in range(1, cols):
            maxValue[0][j] = maxValue[0][j-1] + Arr[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                maxValue[i][j] = max(maxValue[i-1][j], maxValue[i][j-1]) + Arr[i][j]
        return maxValue[rows-1][cols-1]

    def getMaxValue3(self, Arr, rows, cols):
        """ 动态规划：构造一维动态规划矩阵，也须双层循环——采用每一行的前一个数覆盖后一个数，降低内存消耗，好方法
        """
        if Arr or rows<=0 or cols<=0:
            return 0
        maxValue_array = [0 for i in range(cols)]
        maxValue_array[0] = Arr[0][0]
        for i in range(1,rows):
            maxValue_array[i] = maxValue_array[i-1] + Arr[i][0]

        for i in range(1, rows):
            for j in range(cols):
                maxValue_array[j] = max(maxValue_array[j], maxValue_array[j-1]) + Arr[i][j]     # maxValue_array[j]在被覆盖之前还是动态规划矩阵上面的位置，即此处为向下走
        return maxValue_array[cols-1]   #即取最后一个位置的数

if __name__ == "__main__":
    a = Solution()
    Arr = [[1,10,3,8], [12,2,9,5], [5,7,4,11], [3,7,16,5]]
    # Arr = [1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5]     # 矩阵也有可能是这种形式，只是Arr[i][j] -> Arr[i*cols + 1]
    rows = len(Arr[0])
    cols = len(Arr)
    print("初始礼物矩阵为：")
    for i in range(rows):
        print(Arr[i])
    maxValue_ = a.getMaxValue2(Arr, rows, cols)
    print("矩阵中从左上角到右下角的最大礼物价值为：\n",maxValue_)
