## 题目描述：给定学生人数，老师给每个学生一个分数，要求每个学生至少分一个饼干，分数高的必须比分数低的学生分得更多的饼干，求老师至少得买多少个饼干？

## 思路：贪心算法，首先给每个学生初始化为1，然后从左往右遍历一次，凡是右边学生分数比左边分数大时，就给右边学生加一个饼干；接着从右往左遍历一次，凡是左边学生分数比右边学生分数大时，就给左边学生加一个饼干。

class Solution:
    """ 分饼干
    """
    def buyMinNum(self, N, Arr):
        """ 搜索法+排列组合
        """
        # 1、初始化一次
        nums = [1]*N

        # 2、从后往前数
        for i in range(0, N-1):
            if Arr[i]<Arr[i+1]:
                nums[i+1] = nums[i]+1
        print(nums)

        # 2、从前往后数
        for i in range(N-1, 1, -1):
            if Arr[i] < Arr[i-1] and nums[i] >= nums[i-1]:
                nums[i-1] = nums[i] + 1
        return sum(nums)

if __name__ == "__main__":
    # 1、输入人数和数组
    N = int(input())
    Arr = list(map(int, input().split()))
    
    # 2、计算最少数量
    a = Solution()
    num = a.buyMinNum(N,Arr)
    print(num)

## 测试用例：
# 输入：
# 6
# 3 6 2 5 6 2
# 输出：
# 10

