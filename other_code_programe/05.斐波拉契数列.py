## 斐波那契数列，剑前n个数据全部打印出来
class Solution:
    def Fibonacci(self, N):
        m = 0
        n = 1
        a = []
        for i in range(N):
            K = m + n
            a.append(K)
            m = n
            n = K
        return a

N = 30
a = Solution()
print(a.Fibonacci(N))