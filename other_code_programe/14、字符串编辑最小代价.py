## 题目：字符串编辑最小代价
## 类型：字符串，最小代价，经典动态规划题型
## 题目作用：

## 题目描述：字符串A编辑成字符串B可有三种操作： 插入、删除、修改，对应的代价为c0，c1，c2，给出字符串A和字符串B以及各自长度m、n，返回字符串A编辑成字符串B的最小代价。

## 核心：如何建立动态规划，以及如何理解每一步的操作。
## 思路：由于计算两个字符串之间互相进行操作的最小代价，因此属于动态规划题型，可以理解最优路径问题。首先建立一个横向长度为str1长度、纵向长度为str2长度的矩阵dp[N][M]；然后分别计算假设str1为空时的代价和str2为空的代价，即第一行第一列；接着计算除去第一行第一列之后的剩余的位置的总代价，例如计算dp[i][j]：1、当str1[i]==str[j]，即新增了两个一样的字符，则dp[i][j]=dp[i-1][j-1]，即无代价；2、当str1[i]!=str[j]，会有三种可能，dp[i-1][j]->dp[i][j]，dp[i][j-1]->dp[i][j]，dp[i-1][j-1]->dp[i][j]，分别对应着删除、插入、替换三种操作。
#           ''  'a'  'b'  'c'  'd'  'f'
# ''         [[ 0.  5. 10. 15. 20. 25.]
# 'a'       [ 3.  0. 13. 18. 23. 28.]
# 'b'       [ 6. 11.  0. 21. 26. 31.]
#  '1'      [ 9. 14. 19. 24. 29. 34.]
#  '2'      [12. 17. 22. 27. 32. 37.]
# 'c'       [15. 20. 25. 22. 35. 40.]
#  'd'      [18. 23. 28. 33. 22. 43.]
#  'f'      [21. 26. 31. 36. 41. 22.]]

import numpy as np
class Solution:
    def editString(self, str1, str2, dc, ic, rc):
        str1 = ' ' + str1
        str2 = ' ' + str2
        N = len(str1)
        M = len(str2)
        dp = np.zeros((N, M))
        for i in range(len(str1)):      # 给第一列赋予代价值
            dp[i][0] = dc*i
        for j in range(len(str2)):      # 给第一行赋予代价值
            dp[0][j] = ic*j
        for i in range(1,len(str1)):    # 开始走最优的代价路径  
            for j in range(1, len(str2)):
                if str1[i]!=str2[j]:
                    cost = max(dp[i-1][j]+dc, dp[i][j-1]+ic, dp[i-1][j-1]+rc)
                    dp[i][j] = cost
                else:
                    dp[i][j] = dp[i-1][j-1]
        print(dp)
        minCost = dp[N-1][M-1]
        return minCost

if __name__ == "__main__":
    str1 = "ab12cdf"
    str2  = "abcdf"
    dc, ic, rc = 3, 5, 2        # 删除、插入、替换字符串的代价（可以作为输入）
    a = Solution()
    minCost = a.editString(str1, str2, dc, ic, rc)
    print(minCost)


## 测试用例：
# 输入：
# ab12cdf
# abcdf
# 输出：
# 22
