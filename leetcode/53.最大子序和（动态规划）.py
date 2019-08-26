## 题目：最大子序和（求数值和）
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
        """
        :types nums: List[int]
        :rtype: int
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

    ## 暴力破解法
    def maxSubArray(self, nums) -> int:
        return max_

    ## 分治法
    def maxSubArray3(self, nums) -> int:
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
