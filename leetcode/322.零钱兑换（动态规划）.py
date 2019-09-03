## 题目：零钱兑换
## 类型：动态规划

## 题目描述：给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 扩展：假设每个不同硬币的数量是有限的，例如1,2,5每个硬币只有10个。
# 扩展2：假设每个硬币数量的限制是不同的，例如1,2,3各5个、3个、4个。

## 输入：coins = [1, 2, 5], amount = 11
## 输出：3
## 解释：11 = 5 + 5 + 1


## 思路1（暴力法）：优化目标$min \sum_{i=0}^{n-1} x_{i}}$，其中约束条件为$\sum_{i=0}^{n-1} x_{i} * c_{i} = S$，容易看到$x_{i} = [0, \frac{S}{c_{i}}]$，因此暴力法为枚举所有硬币频率子集[x_{0},...,x_{n-1}}]，然后再满足约束条件的，计算其和并返回其中的最小值。
# 核心：取出花费不同硬币时剩余的最小硬币数，因此需要将总金额减少之后的每个最小硬币数也计算出来。
# 思路：假设f(n)代表要凑齐金额为n所要用的最少硬币数量，那么有：f(n) = min(f(n-c1), f(n-c2),...,f(n-cn)) + 1，其中c1,c2,...,cn为硬币的所有面额。

## 还是不太明白？？？？？？？？？

class Solution:
    def coinChange(self, coins, amount) -> int:
        """ 暴力搜索法
        """
        if (len(coins)==0 or amount<0):
            return
        return self.process(coins, 0, amount)
    def process(self, Arr, index, amount):
        if amount == 0:
            return 0
        if index<len(Arr) and amount>0:
            maxVal = amount//coins[index]    # 每个硬币所对应的最大数量
            minCost = float('inf')
            for x in range(ma)


    def process(self, Arr, index, aim):
        res = 0
        if index==len(Arr):
            if aim==0:      # 钱正好够
                return 1
            else:                 # 钱不够了
                return 0
        else:
            for i in range(len(Arr)):
                print(Arr[i], i, index+1)
                res += self.process(Arr, index+1, aim-Arr[i]*i)
                # print(aim, res)
            return res

    def coinChange2(self, coins, amount) -> int:
        """ 动态规划法
        """
        res = [0 for _ in range(amount+1)]  #res相当于最少硬币数量函数f(n)，总共定义了amount个

        for i in range(1, amount+1):
            cost = float('inf')
            for c in coins:
                if i >= c:
                    cost = min(cost, res[i-c]+1)
            res[i] = cost

        temp = set()
        for elem in res:
            if elem != float('inf'):
                temp.add(elem)
        print(len(temp))
        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]

    def coinChange3(self, coins, amount) -> int:
        """ 记忆搜索法
        """
        return

if __name__ == "__main__":
    coins = [1, 2, 5]   #硬币数量不受限
    amount = 11
    # coins = list(map(int, input().split()))
    # amount = int(input())
    a = Solution()
    minNumber = a.coinChange(coins, amount)
    print(minNumber)

## 测试用例：
# 输入：
# coins = [1, 2, 5], amout = 11
# 输出：
# 3
# 输入：[2,3,5]
# coins = [1, 2, 5], amout = 11
# 输出：
# 3
