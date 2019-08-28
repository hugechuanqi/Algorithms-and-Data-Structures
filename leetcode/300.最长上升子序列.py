## 题目：最长上升子序列
## 类型：二分查找，动态规划
## 应用：

## 题目描述：给定一个无序的整数数组，找到其中最长上升子序列的长度。

## 核心：将该序列从前往后逐次判断长的上升子序列
## 思路：建立一个动态规划的dp数组，然后dp[i]指的就是以i位置为终点计算出来的最长上升子序列，核心内容为maxValue = max(maxValue, dp[j])，也就是如果i之前的值有比i值小时，取出i位置之前的所有dp最大值，然后+1，否则i位置的dp值为1。

## 输入：[10,9,2,5,3,7,101,181]
## 输出：4

class Solution(object):
    def lengthOfLIS(self, Arr):
        length = len(Arr)
        if length==0:
            return
        dp = [0]*length
        dp[0] = 1
        for i in range(1, length):
            maxValue = 0        # 最大dp值，即之前的最长上升子序列
            for j in range(0, i):
                if Arr[i]>Arr[j]:       # 如果当前数比之前的数大，则在dp[i] = dp[j] + 1，即在之前长度上再添加一个数
                    maxValue = max(maxValue, dp[j])
            dp[i] = maxValue + 1
        return dp[length-1]

if __name__ == "__main__":
    Arr = [10,9,2,5,3,7,101,18]
    a = Solution()
    length = a.lengthOfLIS(Arr)
    print(length)

## 测试用例
## 输入：
# [10,9,2,5,3,7,101,18]
## 输出：
# 4