## 题目：零钱兑换
## 类型：动态规划

## 题目描述：给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 扩展：假设每个不同硬币的数量是有限的，例如1,2,5每个硬币只有10个。
# 扩展2：假设每个硬币数量的限制是不同的，例如1,2,3各5个、3个、4个。

## 输入：coins = [1, 2, 5], amount = 11
## 输出：3
## 解释：11 = 5 + 5 + 1

# 核心：取出花费不同硬币时剩余的最小硬币数，因此需要将总金额减少之后的每个最小硬币数也计算出来。
# 思路：假设f(n)代表要凑齐金额为n所要用的最少硬币数量，那么有：f(n) = min(f(n-c1), f(n-c2),...,f(n-cn)) + 1，其中c1,c2,...,cn为硬币的所有面额。

class Solution:
    # 动态规划：复杂度为O(coins*amount)
    def coinChange(self, coins, amount) -> int:
        res = [0 for _ in range(amount+1)]  #res相当于最少硬币数量函数f(n)，总共定义了amount个

        for i in range(1, amount+1):
            cost = float('inf')
            for c in coins:
                if i >= c:
                    cost = min(cost, res[i-c]+1)
            res[i] = cost

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]

if __name__ == "__main__":
    coins = [1, 2, 5]   #硬币数量不受限
    amout = 11
    a = Solution()
    minNumber = a.coinChange(coins, amout)
    print(minNumber)

## 测试用例：
# 输入：
# coins = [1, 2, 5], amout = 11
# 输出：
# 11 = 5 + 5 + 1
