## 题目：购买衣服
## 类型：动态规划（0-1背包问题）


## 题目描述：换季了，小红薯看上许多漂亮的衣服，都想买。但是她预算有限，衣橱大小也有限，希望你帮帮她挑选买哪些。有N件衣服，每件衣服有指定的价格P和价值V（代表小红薯的喜欢程度）每件候选衣服只能买一件，预算B限定了总价格上限，衣橱空间S限定了总件数上限。希望选择合适的衣服组合，使总价值尽量大。当有多个方案总价值相同时，希望总价格尽量小，总价格也相同时，希望购买件数尽量少

## 思路：动态规划，对于每一件衣服遍历衣橱空间，当衣橱空间可以容纳当前衣服时，与之前已放进去的物品所得价值进行对比，考虑把是否需要置换。

import numpy as np
class Solution():
    def BagMaxValue(self, S, B, P, V):
        """ 动态规划：二维矩阵
        """
        rows = len(P)
        cols = B
        dp = [[0 for j in range(cols+1)] for i in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                dp[i][j] = dp[i-1][j]
                if j >= P[i-1] and dp[i][j] < dp[i-1][j - P[i-1]] + V[i-1]:
                    dp[i][j] = dp[i-1][j - P[i-1]] + V[i-1]
        print(np.matrix(dp))        
        return dp

if __name__ == "__main__":
    B = 10      # 总价格上限
    S = 6         # 衣服数量上限——这个很重要
    P = [2,2,3,1,5,2, 3]
    V = [2,3,1,5,4,3, 10]
    a = Solution()
    dp = a.BagMaxValue(S, B, P, V)
    print("最大价值为：", dp[S+1][B])