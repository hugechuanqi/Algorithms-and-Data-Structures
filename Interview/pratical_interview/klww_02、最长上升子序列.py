## 题目：最长上升子序列
## 类型：动态规划

## 题目描述：给定一个无序的整数数组，找到其中最长上升子序列的长度。
## 思路：


## 备注：数组是乱序的
def getMaxSubLength(array, N):
    res = [0]*N
    for i in range(len(array)):
        count = 0
        temp = array[i]
        for j in range(i+1, len(array)):
            if array[j]>temp:
                count += 1
                temp = array[j]
        res[i] = count
    print(res)
    return max(res)

## 正确66.95%
class Solution:
    def lengthOfLIS(self, nums) -> int:
        length = len(nums)
        new_arr = [] # 最长上升子列数组
        if length == 0:  # 原数组为空
            return 0
        elif length == 1:  # 原数组只有一个元素
            return 1
        else:
            new_arr.append(nums[0])
            for i in range(1, length):
                if nums[i] <= new_arr[0]:  # 如果遍历的元素比子列中最小值还小或相等，则替换
                    new_arr[0] = nums[i]
                elif (new_arr[0] < nums[i]) and (nums[i] <= new_arr[-1]):  # 如果遍历的元素值大小在子列中间，则查找到第一个大于或等于此元素的子列元素，进行替换；new_arr目前是已经有序的，所以可以用二分查找提高检索效率
                    low,high = 0,len(new_arr)-1
                    while low <= high:
                        mid = (low+high)//2
                        if new_arr[mid] >= nums[i]:
                            new_arr[mid] = nums[i]
                            break
                        else:
                            low = mid + 1
                elif nums[i] > new_arr[-1]:  # 如果遍历的元素比子列最大元素还大，则追加到子列尾部
                    new_arr.append(nums[i])
            return len(new_arr)

## 正确100%
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l:
            return 0
        dp = [1 for _ in range(l)]
        
        for index, item in enumerate(nums):
            dp[index] = self.find(nums[:index + 1], dp) + 1
        # print dp       
        return max(dp)
            
    
    def find(self, nums, dp):
        max_element = -1 * 2 << 31  # 想到于取无穷大
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[-1]:
                max_element = max(max_element, dp[i]) 
 
        return max_element if max_element != -1 * 2 << 31 else 0

if __name__ == "__main__":
    N = int(input())
    array = []
    for i in range(N):
        array.append(int(input()))
    a = Solution()
    length = a.lengthOfLIS(array)
    print(length)

## 测试用例：
# 输入：
# 8
# 10
# 9
# 2
# 5
# 3
# 7
# 101
# 18
# 输出：
# 4

