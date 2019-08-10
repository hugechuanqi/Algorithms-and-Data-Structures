## 题目：最少纸币张数
## 类型：动态规划

class Solution:
    ## 动态规划
    def minNumber(self, array, amt):
        """
        :types nums: List[int]
        :rtype: int
        """
        nums = [0]*len(array)
        array_new = array[::-1]
        for i in range(len(array_new)):
            if i == len(array_new) and array_new[i] != amt:
                nums[i] = -1
            res = array_new[i]
            num = 1
            if array_new[i] == amt:
                nums[i] = 1
                continue
            elif array_new[i] > amt:
                res = 0
                num = 0
            else:
                for j in range(i+1, len(array_new)):
                    if j==len(array_new) and res+array_new[j] != amt:
                        nums[i] = -1
                    if res+array_new[j] > amt:
                        continue
                    res = res + array_new[j]
                    if res == amt:
                        nums[i] = num+1
                    elif res>amt:
                        res -= array_new[j]
                    else:
                        num += 1

        print(nums)
        nums_new = []
        for i in nums:
            if i!=0 and i!=-1:
                nums_new.append(i)
        if len(nums_new)>0:
            return min(nums_new)
        else:
            return -1

teller = list(map(int, input().split(",")))
amt = int(input())
teller.sort()
a  = Solution()
minNum = a.minNumber(teller, amt)
print(minNum)
# print("最少纸币张数：", mi+nNum)

## 测试用例：
# 输入：
# 5,5,10,1,1,5,100,50,50,50,60,40,20
# 6
# 输出：
# 2
