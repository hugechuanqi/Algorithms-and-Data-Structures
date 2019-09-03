## 题目：最短路径和
## 类型：数组，动态规划（类似于“礼物的最大价值.py”，但与"公共子序列.py"有些差距）

## 题目描述：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。（这里默认只能向下或者向右行走，而不会斜着走）
## 输入：
# [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
# ]
## 输出：7

## 核心：如何建立二维矩阵，是自顶向下，还是自底向上
## 思路：动态规划：自顶向下，建立一个二维矩阵dp[][]，用于存储每一个位置的最短路径和。在这个矩阵中，dp(i,j) 表示从坐标 (i,j)(i, j)(i,j) 到右下角的最小路径权值。我们初始化右下角的 dpdpdp 值为对应的原矩阵值，然后去填整个矩阵，对于每个元素考虑移动到右边或者下面，因此获得最小路径和我们有如下递推公式：
# $$dp(i,j) = grid(i,j) + min(dp(i+1, j), dp(i, j+1))$$

# 参考:https://leetcode-cn.com/problems/minimum-path-sum/solution/java-sou-suo-ji-yi-hua-sou-suo-dp-by-crsm/

class Solution:
    def minPathSum(self, matrix):
        """ 动态规划：自顶向下，建立二维矩阵
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for j in range(cols)] for i in range(rows)]
        dp[0][0] = matrix[0][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + matrix[0][j]
        for i in range(1, rows):
            dp[i][0] = dp[i][0] + matrix[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]   # 取向右走或向下走的最小值

        return dp[rows-1][cols-1]

    def minPathSum2(self, matrix):
        """ 动态规划：自顶向下，建立一维矩阵——节省内存消耗
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [0 for j in range(cols)]
        dp[0] = matrix[0][0]
        for  j in range(cols):
            dp[j] = dp[j-1] + matrix[0][j]

        for  i  in range(1, rows):
            for j in range(cols):
                dp[j] = min(dp[j-1], dp[j]) + matrix[i][j]
        
        return dp[cols-1]

if __name__ == "__main__":
    matrix = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
    a = Solution()
    res = a.minPathSum(matrix)
    print(res)

## 测试用例：
## 输入：
# [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
# ]
## 输出：7
