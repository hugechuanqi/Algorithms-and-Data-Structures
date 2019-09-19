## 题目：背包问题
## 类型：贪心算法，动态规划

## 题目描述：有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的体积是vi，价值是wi，求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
# [背包九讲](https://www.cnblogs.com/jbelial/articles/2116074.html)
# [acwing练题网站](https://www.acwing.com/problem/content/3/)

## 思路1：最简单的想法，就是将完全背包转化为0-1背包问题，可以将第 i 种物品转化为W/w[i]件费用及价值均不变的物品，然后求解0-1背包问题。
## 思路2：更高效的转化方法是第 i 种物品拆成费用为w[i]*2^k，价值为v[i]*2^k的若干件物品，其中k满足w[i]*2^k<=W。因为不管最优策略 选几件第 i 种物品，总可以表示成若干个 2^k 件物品的和（二进制思想）
## 思路3（完全背包优化）：若两件物品i、j满足c[i]<=c[j]且w[i]>=w[j]，则将物品j去掉，不用考虑。c表物品重量，w表示对应物品价值。即将重量大且价值低的物品去掉。
## 思路4（复杂度为O(VN)）： 0-1背包问题中要按照 w=W..0 的逆序来循环，而完全背包必须按照从小到大的顺序。这是因为 要保证第 i 次循环中的状态 f[i][w]是由状态 f[i-1][w-w[i]]递推而来。换句话 说，这正是为了保证每件物品只选一次，保证在考虑“选入第 i 件物品”这件策 略时，依据的是一个绝无已经选入第 i 件物品的子结果 f[i-1][w-w[i]]。而现 在完全背包的特点恰是每种物品可选无限件，所以在考虑“加选一件第 i 种物 品”这种策略时，却正需要一个可能已选入第 i 种物品的子结果 f[i][w-w[i]]， 所以就可以并且必须采用 w=0..W 的顺序循环。
## 伪代码：
# for i=1...N
#   for w=0...W
#       f[w] = max(f[w], f[w-cost]+weight)

class Solution:
    def getdict(self, weight, value):
        """ 0-1背包转为完全背包问题：有限变无限
        """
        weightValue = {}
        for i in range(len(weight)):
            key = weight[i]
            if key not in weightValue.keys():
                weightValue[key] = value[i]
            elif value[i] > weightValue[key]:
                weightValue[key] = value[i]
            else:
                continue

        print("物品体积价值对应比：", weightValue, list(weightValue.items()))
        weight_new = list(weightValue.keys())   # [2,3,1,5]
        value_new = list(weightValue.values())    # [3,1,5,4]
        print("物品重量为：", weight_new, "物品价值为：", value_new)
        return weight_new, value_new

    def BagMaxValue(self, num, WeightLimit,  weight, value):
        """ 完全背包问题
        """
        rows = len(weight)
        cols = WeightLimit
        dp = [0 for j in range(cols+1)]

        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if j>=weight[i-1]:
                    print(j)
                    dp[j] = max(dp[j], dp[j-weight[i-1]] + value[i-1])
        import numpy as np
        print(np.matrix(dp))
        return dp

if __name__ == "__main__":
    # 1、完全背包问题
    num = 6         # 物品数量
    WeightLimit = 10        # 书包能承受的体积
    weight = [2,2,3,1,5,2]     # 每个物品的体积
    value = [2,3,1,5,4,3]         # 每个物品的价值
   
    a = Solution()
    weight_new, value_new = a.getdict(weight, value)

    rows = len(weight_new)
    dp = a.BagMaxValue(num, WeightLimit, weight_new, value_new)
    print("背包最大价值为：", dp[WeightLimit])




