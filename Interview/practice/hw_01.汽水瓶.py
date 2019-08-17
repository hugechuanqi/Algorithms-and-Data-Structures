## 题目：汽水瓶（空汽水瓶更换的数目）
## 类型：数组
## 题目描述：
# 某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？

## 输入:输入文件最多包含10组测试数据，每个数据占一行，仅包含一个正整数n（1<=n<=100），表示小张手上的空汽水瓶数。n=0表示输入结束，你的程序不应当处理这一行。
## 输出:对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

# - 核心：你最后可以向老板再借一瓶，这个条件真是太有灵魂了。
# - 思路：（1）假设初始瓶子数全是满的，计算最终能够喝水的瓶子数，然后再减去初始瓶子数；（2）由于初始瓶子数全是空的，因此我们只计算能够换来的瓶子数。因此每次更换时的瓶子数就是我们要的结果。


# 牛客网解答1：通过数学分析，最后获得的饮料数是总空瓶数整除2 。即每两个汽水瓶换一个，所以除以2就行了。
class Solution:
    def __init__(self, nn=0,res=0):
        self.n = nn
        self.res = res

    ## 递归实现——暂时有点问题
    def can_drink(self):
        print("初始值:",self.n)
        if self.n==1:
            return self.n
        if self.n==2:
            return self.n + 1
        if self.n>=3:
            m = self.n%3
            # a = n//3
            self.res =  3*(self.n//3) + self.can_drink(self.n//3+m)
            # print(res)
        return self.res

    ## 能够喝的瓶子数，包括原始的瓶子数（非递归）——本人最原始方法
    def can_drink2(self, n):
        # 当剩下的瓶子树小于3时，就不允许更换
        if n<3:
            return n
        res = 0
        # 当剩下的瓶子数大于等于3时，就可以换一次
        while(n>=3):
            m = n%3
            res =  res + 3*(n//3)   #能喝的瓶子数
            n = n//3 + m    #剩下的瓶子数
            if n==2:
                res = res + n + 1
            elif n==1:
                res = res + n
        return res

    ## 这里的res只包括剩下能换来的瓶子数
    def can_drink3(self, n):
        res = 0
        while(n>=3):
            a = n//3
            m = n%3
            res = res + a
            n = a + m
        if n == 2:
            res = res + 1
        if n == 1:
            res = res + 0
        return res

## 官方标准的多个case的输入输出
import sys
a = Solution(20,0)
for line in sys.stdin:
    a_in = line.split()
    water_number = int(a_in[0])
    if water_number == 0:
        break
    # res = a.can_drink() - water_number
    # res = a.can_drink2(water_number) - water_number
    res = a.can_drink3(water_number)
    print(res)

# water_number = int(input())
# res = can_drink(water_number) - water_number
# print(res)

## 测试用例:
# 输入:
# 3
# 10
# 81
# 94
# 0
# 输出:
#1
# 5
# 40
# 47