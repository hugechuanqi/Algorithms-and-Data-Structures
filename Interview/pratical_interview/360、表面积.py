## 题目：表面积
## 类型：三视图

## 题目描述：
## 思路：


import numpy as np
def get_num(nums):
    a1, a2, a3 = 0, 0, 0
    for num1 in nums:
        for a in num1:
            if a!=0:
                a1 += 1
    a2 = 0
    for num1 in nums:
        a2 += max(num1)
    array = np.array(nums)
    length_M = len(nums[0])
    for j in range(length_M):
        a3 = a3+max(array[:,j])

    ss = (a1+a2+a3)*2
    return ss

N, M = list(map(int, input().split()))
nums = []
for i in range(N):
    nums.append(list(map(int, input().split())))
ss = get_num(nums)
print(ss)

## 测试用例;
# 输入：
# 2 2
# 2 1
# 2 2
# 输出：
# 20