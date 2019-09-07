## 题目：数组查找
## 找到第一个缺失的正整数

class Solution:
    def getHeadNum(self, Arr, N):
        if 1 not in Arr:
            return 1
        if N == 1:
            return 2
        
        for i in range(N):
            if Arr[i] <= 0 or Arr[i] > N:
                Arr[i] = 1
        for i in range(N): 
            a = abs(Arr[i])
            if a == N:
                Arr[0] = - abs(Arr[0])
            else:
                Arr[a] = - abs(Arr[a])
        for i in range(1, N):
            if Arr[i] > 0:
                return i
        
        if Arr[0] > 0:
            return N            
        return N+1

if __name__ == "__main__":
    N = int(input())
    Arr = list(map(int, input().split()))
    a = Solution()
    res = a.getHeadNum(Arr, N)
    print(res)

## 测试用例：
# 输入：
# 4
# 3 4 -1 1
# 输出：
# 2
