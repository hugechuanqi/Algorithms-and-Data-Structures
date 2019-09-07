## 题目：环形数组循环
## 类型：数组、双指针
## 应用：检测某个数组中是否存在环形

## 题目描述：给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k 个索引。因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 > 1。
## 此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说，一个循环中不能同时包括向前的运动和向后的运动。

## 输入：[2,-1,1,2,2]
# 输出：true
# 解释：存在循环，按索引 0 -> 2 -> 3 -> 0 。循环长度为 3 。

## 核心：
## 思路：这个题先放一放

class Solution:
    # def checkRingArr(self, i, Arr):
    #     p = i + Arr[i]
    #     i = 0
    #     while(i<len(Arr)):
    #         print("--", p)
    #         p = p%len(Arr)
    #         if p==i  and (Arr[p] and Arr[i]):
    #             return True
    #         elif p!=i:
    #             p = p + Arr[i]
    #             i += Arr[i]
    #         else:       # 即构成死循环
    #             break
    #     return False

    def circularArrayLoop(self, Arr):
        """ DFS：深度优先搜索
        """
        n = len(Arr)
        visited = set()     # 用于存储已经访问到的结点
        for i in range(n):
            if i not in visited:
                direction = Arr[i]     # 记录正反向
                visited.add(i)
                numSet = set()      # 存储某次可能环形数组中的位置
                numSet.add(i)
                j = (i + Arr[i])%n     # 下一个位置

                while(j not in visited):
                    visited.add(j)
                    if Arr[j] * direction < 0:      # 表示方向不同，则从下一个方向开始
                        direction = Arr[j]
                        numSet = set()
                        numSet.add(j)
                        j = (n+j+Arr[j])%n
                    else:
                        numSet.add(j)
                        j = (n+j+Arr[j])%n

                    if j in numSet and len(numSet)>=2:      # 表示如果当前位置在本次环形数组中
                        return True
        return False

if __name__ == "__main__":
    # Arr = list(map(int, input().split()))
    Arr = eval(input())
    a = Solution()
    print(a.circularArrayLoop(Arr))

## 测试用例：
# 输入：[2,-1,1,2,2]
# 输出：true
# 输入：[-2,1,-1,-2,-2]
# 输出：False

