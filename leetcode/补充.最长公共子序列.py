## 题目：最长公共子序列
## 类型：动态规划，Dp数组

class LCS:
    def findLCS(self, str1, str2):
        """ 动态规划DP
        """
        n = len(str1)
        m = len(str2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

if __name__ == "__main__":
    str1 = "abcdefghiklmnop"
    str2 = "abcddefjklmnopqrstuv"
    a = LCS()
    res = a.findLCS(str1, str2)
    print(res)

## 测试用例：
# 输入：
# "abcdefghiklmnop"
# "abcddefjklmnopqrstuv"
# 输出：
# 12
