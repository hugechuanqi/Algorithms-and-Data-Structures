## 题目：环形数组循环
## 类型：数组、双指针
## 应用：检测某个数组中是否存在环形

## 题目描述：给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k 个索引。因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 > 1。
## 此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说，一个循环中不能同时包括向前的运动和向后的运动。

## 输入：[2,-1,1,2,2]
# 输出：true
# 解释：存在循环，按索引 0 -> 2 -> 3 -> 0 。循环长度为 3 。

## 核心：访问结点数组+环形数组+方向标记
## 思路：首先，建立两个数组vistited和numSet，分别表示存储被访问过的结点和可能环形数组的结点；然后遍历所有结点，建立一个标签direction，表示当前结点的方向，一旦发生方向不同的结点，则需要将numSet置0，否则将当前结点加入至numSet，并根据当前结点判断以该结点为起点是否能构成一个环形数组（方向一直的环）。如果能就返回true，否则访问下一个结点。

class Solution:
    def checkLoop(self, j, Arr, visited, numSet, direction):
        """ 双指针：以j为起点判断是否可能构成环形数组，direction存储着当前指针的方向，j表示另一个移动指针
        """
        n = len(Arr)
        while(j not in visited):
            visited.add(j)
            if Arr[j] * direction < 0:      # 表示方向不同，则从下一个方向开始（一旦方向不同，则表明numSet存储的结点不能构成环形，因此需要置0）
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

    def circularArrayLoop(self, Arr):
        """ DFS：深度优先搜索
        """
        n = len(Arr)
        visited = set()     # 用于存储已经访问到的结点，字典的
        for i in range(n):
            if i not in visited:
                direction = Arr[i]     # 记录正反向
                visited.add(i)
                numSet = set()      # 存储某次可能环形数组中的位置
                numSet.add(i)
                j = (i + Arr[i])%n     # 下一个位置
                if self.checkLoop(j, Arr, visited, numSet, direction):
                    return True
        return False

if __name__ == "__main__":
    # Arr = list(map(int, input().split()))
    # Arr = eval(input())
    Arr = [2,-1,1,2,2]
    a = Solution()
    print(a.circularArrayLoop(Arr))

## 测试用例：
# 输入：[2,-1,1,2,2]
# 输出：true
# 输入：[-2,1,-1,-2,-2]
# 输出：False

