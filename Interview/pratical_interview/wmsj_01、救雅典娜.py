## 题目：救雅典娜
## 类型：回溯法，动态规划

## 题目描述：从矩阵左上角走到矩阵右下角的最小代价，并且中途的血量不能少于1。

## 思路：每走一步，将当前位置的数与之前走过的最短路径进行叠加，并进行比较。(但这只是局部最优，没有达到全局最优)
## 核心：需要限制边界值

## 最短路径参考：https://www.cnblogs.com/Lee-yl/p/9973770.html

class Solution:
    def minblood(self, n,m,array,first):
        if n<=1 or m<=1:
            return sum(array)
        # for i in range(1, n):
        #     array[i*m+0] = array[i*m]+array[(i-1)*m]
        # for j in range(1,m):
        #     array[j] = array[j] + array[j-1]
        print(array)
        for i in range(0,n-1):
            for j in range(0,m-1):
                sum_right = array[i*m + (j+1)] + array[i*m + j] 
                sum_down = array[(i+1)*m + j] + array[i*m + j]
                print("++", sum_right+first, sum_down+first)

                if sum_right+first<1 and sum_down+first<1:
                    return -1,-1
                elif sum_right+first>=1 and sum_down+first<1:
                    array[i*m+j] = sum_right
                elif sum_right+first<1 and sum_down+first>=1:
                    array[i*m+j] = sum_down
                else:
                    if sum_right>sum_down:
                        array[i*m+j] = sum_right
                    else:
                        array[i*m+j] = sum_down
        return 1,-array[(n-1)*m+m-1]+1

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    array = list(map(int, input().split()))
    a = Solution()
    
    for first in range(-min(array)):
        print(first, -min(array))
        array1 = array.copy()
        flag, res = a.minblood(n,m,array1,first)
        print(flag, res)
        if flag==-1:
            continue
        elif flag ==1:
            break
    print(res)

## 测试用例：
# 输入：
# 3
# 3
# -2 -3 3 -5 -10 1 0 30 -5
# 输出：
# 7

