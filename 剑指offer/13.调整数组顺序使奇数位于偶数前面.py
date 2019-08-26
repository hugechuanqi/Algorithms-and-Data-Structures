## 题目：调整数组顺序使奇数位于偶数前面
## 类型：数组

## 题目描述：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

## 思路：新建两个数组，遍历原始数组，将奇数依次存储进入数组1，将偶数依次存储进入数组2，然后将两个数组合并

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        oddNum = []
        evenNum = []
        for elem in array:
            if elem%2==0:
                oddNum.append(elem)
            else:
                evenNum.append(elem)
        evenNum.extend(oddNum)
        return evenNum

if __name__ == "__main__":
    Arr = [1,2,3,4,5,6,7]
    a = Solution()
    res = a.reOrderArray(Arr)
    print(res)


