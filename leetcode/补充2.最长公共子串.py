## 题目：最长公共子串
## 类型：字符串，动态规划


## 思路：动态规划

class Solution:
    """ 最长公共子串"""
    def LCS(self, str1, str2):
        """ 动态规划：记录每次动态规划之后所有的值
        """
        dp = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
        maxLength = 0
        p = 0
        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > maxLength:
                        maxLength = dp[i][j]
                        p = i-1       # 指向最后一个相同的子串位置
        return str1[p+1-maxLength: p+1]

if __name__ == "__main__":
    str1 = "abcdfg"
    str2 = "abdfg"
    a = Solution()
    res = a.LCS(str1, str2)
    print(res)
