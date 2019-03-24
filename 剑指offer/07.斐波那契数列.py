# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        f0 = 0
        f1 = 1
        if n==0:
            return 0
        if n==1:
            return 1
        while n>1:
            fn = f0 + f1
            f0 = f1
            f1 = fn
            n = n - 1
        return fn

## 测试用例
n = 10
a = Solution()
print(a.Fibonacci(n))