## 题目：小Q修栏栅
## 类型：动态规划

## 题目描述：获取最短子序列
## 思路：

class Solution:
    ## 动态规划
    def minSubArray(self, array, k):
        minSumList = [10000000]*len(array)
        for i in range(len(array)):
            sum_ = 0
            for j in range(i, i+k):
                if j<len(array):
                    sum_ += array[j]
                else:
                    sum_ += array[j-len(array)]
            minSumList[i] = sum_
        return min(minSumList)

    def minSubArray2(self, array, k):
        minSumList = [10000000]*len(array)
        for i in range(len(array)):
            if i+k<len(array):
                minSumList[i] = sum(array[i:i+k])
        index_ = minSumList.index(min(minSumList))
        return index_+1


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    a  = Solution()
    minSum = a.minSubArray2(array, k)
    print(minSum)

## 测试用例：
# 输入：
# 7 3
# 1 2 6 1 1 7 1
# 输出：
# 3

## 02拆零件
## 03奥利奥冰淇淋
## 04航线
## 05探险