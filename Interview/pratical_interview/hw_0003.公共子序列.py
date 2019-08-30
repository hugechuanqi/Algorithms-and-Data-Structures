## 题目：相当于最长公共子序列
## 类型：字符串，动态规划
## 题目应用：

## 题目描述：给定两个字符串，要求删除即个字符后，能够让这两个字符串相等，求最少需要删除多少个字符才能完成
## 核心：对于两个字符串，进行比较操作时，需要建立一个矩阵，每次增加字符串时就更新一下最后的最长公共字符串状态dp[i][j]。
## 思路：1、首先利用动态规划建立一个(n+1)*(m+1)的矩阵dp，第一行第一列全部为0，2、然后利用动态规划，依次判断下一个状态是由前一个状态转换而来，包括三种情况：第一种当A[i]=B[j]时（此处由于第一行第一列无实际意义因此为p-1和q-1），则可以直接在dp[i][j] = dp[i-1][j-1]+1，第二种情况，当前状态dp[i][j]由前一个状态dp[i-1][j]或dp[i][j-1]转移而来，但是由于没有新增任何相等的字符，因此无需+1处理。最后直到移动到dp[n][m]则表明状态已经转移到A[n],B[m]处，完成最长公共自序列长度的获取

class LCS:
    def findLCS(self, A, B):
        """ 最长公共子序列
        """
        n = len(A)
        m = len(B)
        table=[[0 for i in range(m+1)] for j in range(n+1)]
        for p in range(1,n+1):
            for q in range(1,m+1):
                if A[p-1]==B[q-1]:
                    table[p][q]=table[p-1][q-1]+1
                else:
                    table[p][q]=max(table[p-1][q],table[p][q-1])
        return table[n][m]

if __name__ == "__main__":
    n = int(input())
    str1 = list(map(int, input().split()))
    str2 = list(map(int, input().split()))
    a = LCS()
    length = a.findLCS(str1, str2)
    print(n-length)

## 测试用例：
# 输入：
# [a,b,c,d,e,f,g]
# [a,c,h,g]
# 输出：
# [3]
# [a,c,g]
## 由于此处题目时要求字符串str1和str2字符串长度一致，求需要删除的最少长度，例如
# 输入：
# 7
# [a,b,c,d,e,f,g]
# [b,c,i,k,e,h,g]
# 输出：
# 3（最长公共子序列长度为4，因此各需要至少删除3个字符）
