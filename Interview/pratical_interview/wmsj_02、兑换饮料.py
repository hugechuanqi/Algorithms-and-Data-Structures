## 题目：兑换饮料
## 类型：动态规划，数组（和硬币拼凑一致）

## 思路：利用动态

class Solution:
    def getminNum(self, Arr, key):
        res = [0 for _ in range(key+1)]

        for i in range(1, key+1):   # 计算key之前所有数值的可能性
            cost = float('inf')
            for c in Arr:
                if i >= c:
                    cost = min(cost, res[i-c]+1)
            res[i] = cost

        if res[key] == float('inf'):
            return -1
        else:
            return res[key]

if __name__ == "__main__":
    n = int(input())
    Arr = list(map(int, input().split()))
    key = int(input())
    a = Solution() 
    minNum = a.getminNum(Arr, key)
    print(minNum)

## 测试用例
# 输入
# 3
# 5 2 3
# 20
# 输出
# 4