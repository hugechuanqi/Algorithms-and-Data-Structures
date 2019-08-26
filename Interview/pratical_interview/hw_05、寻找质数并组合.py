## 题目：寻找质数并组合
## 类型：数组，质数

## 思路：首选判断区间内的每个数是否为质数，然后将每个质数的个位数提取出来相加，将质数的10位数提取出来相加，最后进行比较即可。

## 寻找质数并组合
class Solution:
    def is_prime(self, num):
        if num<=1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

    def getPrimes(self, left, right):
        res = []
        for num in range(left, right):
            if self.is_prime(num):
                res.append(num)
        print(res)
        oneNum = 0
        tenNum = 0
        for elem in res:
            if elem<=9:
                oneNum += elem
            else:
                oneNum += int(str(elem)[-1])
                tenNum += int(str(elem)[-2])
        return min(oneNum, tenNum)

if __name__ == "__main__":
    left, rigth = list(map(int, input().split()))
    a = Solution()
    minNum = a.getPrimes(left, rigth)
    print(minNum)

##测试用例：
# 输入：
# 151 160
# 输出（151，157）：
# 8
# 输入：
# 1 15
# 输出
# 2