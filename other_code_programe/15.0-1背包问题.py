## 题目：背包问题
## 类型：贪心算法，动态规划

## 题目描述1：给定一组物品，每种物品都有自己的重量和价值，在限定的总重量内，我们如何选择，才能使得物品的总价值最高。背包容量：C＝50千克。3件物品。物品1重20千克，价值100元；物品2重20千克，价值120元；物品3重30千克，价值90元。

## 参考：https://blog.csdn.net/qq_34178562/article/details/79959380
## 递归定义：
# ![0-1背包](https://img-blog.csdn.net/20180416130127370?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MTc4NTYy/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
# [背包九讲](https://www.cnblogs.com/jbelial/articles/2116074.html)


## 核心：学会如何建模，由于限定总数量，背包容纳数量，目标时达到背包价值最大化，过程中之需要控制重量符合要求即可。
## 思路1：动态规划，对于每一件物品遍历背包容量，当背包可容纳值大于等于当前物品，与之前已放进去的物品所得价值进行对比，考虑把是否需要置换。

## 状态转移方程：定义dp[i][j]：前i个物品，背包容量j下的最优解
# （1）当前背包容量不够，为前$i-1$个物品最优解：j<w[i]时，有dp[i][j]=dp[i-1][j]
# （2）当前背包容量够，判断选还是不选第i个物品：j>=w[i]时，选该物品->dp[i][j]=dp[i-1][j-w[i]]+v[i]；不选该物品->dp[i][j]=dp[i-1][j]
## 伪代码：（对应一维矩阵解法）
# for i=1..N
#   for v=V..0
#       f[v]=max{f[v],f[v-c[i]]+w[i]}; 

## 题目描述2：求出放进哪些物品能使背包价值最高，即输出价值最高时背包里的物品。
## 思路2：输出背包里所放的物品，只需从尾遍历物品，当value大于上一行同样位置的value时，表示放进该物品——因为矩阵最后一个价值增大的位置一定是放了物品的位置，然后不断往前推即可。（但是只有建立了二维矩阵的数组才能根据所取物品位置）

import numpy as np
class Solution:
    """ 0-1背包问题：获取最大价值
    """
    def BagMaxValue(self, weightLimit, weight, value):
        """ 动态规划：二维矩阵，获取最大价值，时间复杂度O(rows*cols)，空间复杂度O(rows*cols)
        """
        rows = len(weight)      # 物品数量，
        cols = weightLimit      # 背包承受重量
        dp = [[0 for j in range(cols+1)] for i in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if j<weight[i-1]:
                    dp[i][j] = dp[i-1][j]
                if j>=weight[i-1] and dp[i][j] < dp[i-1][j-weight[i-1]] + value[i-1]:      # weight[i-1]表示添加的第i-1个物品的重量，v[i-1][j-weight[i-1]]表示有i-1个数量物品，剩余重量为j-weight[i-1]对应的价值
                    dp[i][j] = dp[i-1][j-weight[i-1]] + value[i-1]
        print(np.matrix(dp))
        return dp

    def BagShowIndex(self,  num, weightLimit, weight, dp):
        """ 从尾开始遍历，获取最大价值的物品位置
        """
        rows = num
        cols = weightLimit
        # print("最大价值为：",  dp[rows][cols])
        x = [False for i in range(rows)]
        j = cols
        for i in range(rows,0,-1):
            if dp[i][j] > dp[i-1][j]:
                x[i-1] = True
                j = j - weight[i-1]

        # print("背包中所装物品为：")
        res = []
        for i in range(rows):
            if x[i]:
                # print("第", i+1, "个", end='; ')
                res.append(i+1)
        return res

    def BagMaxValue2(self, num, weightLimit, weight, value):
        """ 动态规划(优化版)：一维矩阵，时间复杂度为O(rows*cols)，空间复杂度为O(rows)
        """
        rows = num               # 所有物品数量
        cols = weightLimit  # 最大承受重量
        dp = [0 for i in range(cols+1)]
        for i in range(1, rows+1):
            for  j in range(cols, 0, -1):
                if j>=weight[i-1]:
                    dp[j] = max(dp[j-weight[i-1]] + value[i-1], dp[j])
        return dp

if __name__ == "__main__":
    # 1、0-1背包问题
    num = 6         # 物品数量
    weightLimit = 10        # 书包能承受的重量
    weight  = [2,2,3,1,5,2]     # 每个物品的重量
    value = [2,3,1,5,4,3]         # 每个物品的价值
    a = Solution()
    dp = a.BagMaxValue(num, weightLimit, weight, value)
    print("背包最大价值为：", dp[num][weightLimit])
    # print("背包最大价值为：", dp[weightLimit])
    
    resIndex = a.BagShowIndex(num, weightLimit, weight, dp)
    print("\n背包中所装物品为：", resIndex)

## 测试用例;
# 输入：
# nums = 6
# weightLimit = 10
# weight = [2,2,3,1,5,2]
# value = [2,3,1,5,4,3]
# 输出：
# 15
# [2,4,5,6]


    ## 2、完全背包问题


