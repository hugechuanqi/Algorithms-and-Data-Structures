## 题目描述：求矩阵中的最短路径和

class Solution: 
    def minPathSum(self, matrix):
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
    rows = int(input())
    cols = int(input())
    matrix = []
    for i in range(rows):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    a = Solution()
    res = a.minPathSum(matrix)
    print(res)

## 测试用例：
# 输入：
# 3
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 输出：
# 21