## 题目：斐波那契数列
## 类型：递归与循环

## 题目描述：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39 

## 思路：

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        """ 循化实现斐波那契数列
        """
        if n==0:
            return 0
        if n==1:
            return 1
        f0 = 0
        f1 = 1
        while n>1:
            fn = f0 + f1
            f0 = f1
            f1 = fn
            n = n - 1
        return fn

    def Fibonacci2(self, n):
        """ 递归实现斐波那契数列
        """
        if n==0:
            return 0
        if n==1:
            return 1
        f0 = 0
        f1 = 1
        return self.process(f0, f1, 2, n)
    def process(self, f0,f1, i, n):
        if i >n:        # i从2开始到n
            return f1
        fn = f0 + f1
        return self.process(f1, fn, i+1, n)

if __name__ == "__main__":
    ## 测试用例
    n = 10
    a = Solution()
    print(a.Fibonacci2(n))

## 测试用例：
# 输入：n=10
# 输出：55
