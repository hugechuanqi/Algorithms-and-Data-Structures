## 题目：前K个高频元素
## 类型：堆，哈希表，优先队列

## 题目描述：给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
## 输入：nums = [1,1,1,2,2,3], k = 2
## 输出：[1,2]

    # 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    # 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。


## 思路：首先建立哈希表，计算出频率，然后根据频率进行堆调整，取前K大的频率，对应哈希表返回元素。

class Solution:
    """ 求TopK：数组中前K个高频元素
    """
    def TopK(self, nums, k):
        """ 一般排序方法
        """
        numSet = {}
        Count = []
        for elem in set(nums):
            num = nums.count(elem)
            numSet[elem] = num
            Count.append(num)
        
        Count.sort(reversed = True)
        result = []
        for i in range(k):
            num = Count[i]
            numSet[num]

    def TopK2(self, nums, k):
        """ 最小堆
        """



if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    a = Solution()
    res = a.TopK(nums, k)
    print(res)

## 测试用例：
# 输入：
# nums = [1,1,1,,2,2,3]
# k = 2
# 输出：
# [1,2]