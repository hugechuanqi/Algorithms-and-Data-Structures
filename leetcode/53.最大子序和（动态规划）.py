## 题目：最大子序和（求最大连续子序和）
## 类型：动态规划，数组，分治算法

## 题目描述：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

## 输入：[-2,1,-3,4,-1,2,1,-5,4]
## 输出：6
#def maxSubArray(self, nums: List[int]) -> int:表示nums为List类型，每个元素为int，-> int表示返回类型为int

## 核心：
## 思路：以数组中的每个值为起点，遍历数组，计算以该值为起点的子序的最大数值，最后对比得出以哪个值为起点的子序值最大

class Solution:
    ## 动态规划
    def maxSubArray(self, array):
        """ 暴力求解法
        """
        maxSumList = [0]*len(array)
        for i in range(len(array)):
            maxSum = 0
            sum_ = 0
            for j in range(i, len(array)):
                sum_ += array[j]
                # print(i, sum_)
                if maxSum < sum_:
                    maxSum = sum_
            maxSumList[i] = maxSum
            
        return max(maxSumList)

    def maxSubArray(self, nums) -> int:
        """ 动态规划法DP
        """
        tmp = nums[0]   # 假设最大子序和从第一个开始
        max_  = tmp
        for i in range(1, len(nums)):
            if tmp+nums[i] > nums[i]:       # 如果当前序列加上次时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
            else:       # 如果tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列，并记录此时的最大值
                max_ = max(max_, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]

        return max_

    def maxSubArray3(self, nums) -> int:
        """ 分治法：将数组分为左右两部分和中间部分，递归实现。没能完全理解
        """
        n = len(nums)
        if n==1:
            return nums[0]
        else:
            max_left = self.maxSubArray3(nums[0:len(nums)//2])
            max_right = self.maxSubArray3(nums[len(nums)//2:len(nums)])

        max_l = nums[len(nums)//2 - 1]
        tmp = 0
        for i in range(len(nums)//2 - 1 , -1, -1):
            tmp += nums[i]
            max_l = max(max_l, tmp)
        max_r = nums[len(nums)//2]
        tmp = 0
        for i in range(len(nums)//2, len(nums)):
            tmp += nums[i]
            max_r = max(max_r, tmp)
        return max(max_right, max_left, max_l+max_r)
        
if __name__ == "__main__":
    # array = eval(input())
    array = [-2,1,-3,4,-1,2,1,-5,4]
    print(array[0])
    a  = Solution()
    maxSum = a.maxSubArray3(array)
    print("最大子序和为：", maxSum)

## 测试用例：
# 输入：[-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
