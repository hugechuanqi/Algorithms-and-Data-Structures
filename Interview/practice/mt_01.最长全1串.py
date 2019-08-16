## 题目：最长全1串
## 类型：动态规划+贪心算法
## 公司：美团

## 题目描述：给你一个01字符串，定义答案=该串中最长的连续1的长度，现在你有至多K次机会，每次机会可以将串中的某个0改成1，现在问最大的可能答案

## 输入：
# 输入第一行两个整数N,K，表示字符串长度和机会次数
# 第二行输入N个整数，表示该字符串的元素
# ( 1 <= N <= 300000
# , 0 <= K <= N )
## 输出：
# 输出一行表示答案

# 思路1：滑动窗口，窗口长度代表最长全1串的长度

def maxSolutionNumber(n, k, num):
    i,j =0,0
    res = 0
    while j<n:
        if num[j]==1:
            j += 1
        elif k > 0:
            k -= 1
            j += 1
        else:
            res = max(res,j-i)
            while i<j and num[i]==1:
                i += 1
            j += 1
            i += 1
    res = max(res,j-i)
    return res

N, K = list(map(int, input().split()))
s = list(map(int, input().split()))
res = maxSolutionNumber(N, K, s)
print(res)


## 测试用例：
# 输入：
# 10 2
# 1 0 0 1 0 1 0 1 0 1
# 输出：
# 5


