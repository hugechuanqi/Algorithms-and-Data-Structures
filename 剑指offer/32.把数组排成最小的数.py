## 题目：把数组排成最小的数
## 类型：数组

## 题目描述：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
## 输入：
## 输出：

## 核心：
## 思路：


# -*- coding:utf-8 -*-
class getLargest(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largest(self, Arr):
        largest_num = ''.join(sorted(map(str, Arr), key=getLargest))
        return '0' if largest_num[0] == '0' else largest_num

if __name__ == "__main__":
    # N = int(input())
    # Arr = list(map(int, input().split()))
    Arr = [30, 1]
    a = Solution()
    res = a.largest(Arr)
    print(res)

