## 题目：排列计数（暴力超时，改了还是超时）
## 类型：全排列
## 应用：此题对应leetcode第903题

## 思路：排列->取出每一个排列->循环比较

class Solution:
    def __init__(self):
        self.count = 0
    def Permutation(self, Arr, A):
        """ DFS：字符串全排列（深度优先搜索）
        """
        result = []
        minNum = A.count(1)
        # count = 0
        if Arr or len(Arr)>0:
            self.perm(0, Arr, result, A, minNum)
        return self.count
    def perm(self, i, Arr, result, A, minNum):
        if i==len(Arr)-1 and Arr[0]>minNum:
            temp = Arr.copy()   # 深度复制很重要
            print(temp, Arr)
            if self.checkOK(A, temp):
                self.count += 1
            # result.append(temp)
        else:
            for j in range(i, len(Arr)):          
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])
                if Arr[0]>minNum:
                    self.perm(i+1, Arr, result, A, minNum)
                else:
                    continue
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])

    def checkOK(self, A, p):
        N = len(p)
        for i in range(N-1):
            if A[i]==0 and p[i]>=p[i+1]:
                return False
            if A[i]==1 and p[i]<=p[i+1]:
                return False
        return True

    # def checkperm(self, N, A, result):
    #     count = 0
    #     for j in range(len(result)):
    #         p = result[j]
    #         if self.checkOK(A, p):
    #             count += 1
    #     return count

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    Arr = [i+1 for i in range(N)]

    a = Solution()
    count = a.Permutation(Arr, A)
    # count = a.checkperm(N, A, result)
    print(count)

## 测试用例：
# 输入：
# 4
# 1 1 0
# 输出：
# 3



# class Solution:
#     def Permutation(self, Arr):
#         """ DFS：字符串全排列（深度优先搜索）
#         """
#         result = []
#         if Arr or len(Arr)>0:
#             self.perm(0, Arr, result)
#         return result
#     def perm(self, i, Arr, result):
#         if i==len(Arr)-1:
#             temp = Arr.copy()   # 深度复制很重要
#             result.append(temp)
#         else:
#             for j in range(i, len(Arr)):
#                 (Arr[i], Arr[j]) = (Arr[j], Arr[i])
#                 self.perm(i+1, Arr, result)
#                 (Arr[i], Arr[j]) = (Arr[j], Arr[i])

#     def checkOK(self, A, p):
#         for i in range(N-1):
#             if A[i]==0 and p[i]>=p[i+1]:
#                 return False
#             if A[i]==1 and p[i]<=p[i+1]:
#                 return False
#         return True

#     def checkperm(self, N, A, result):
#         count = 0
#         for j in range(len(result)):
#             p = result[j]
#             if self.checkOK(A, p):
#                 count += 1
#         return count

# if __name__ == "__main__":
#     N = int(input())
#     A = list(map(int, input().split()))
#     Arr = [i+1 for i in range(N)]

#     a = Solution()
#     result = a.Permutation(Arr)
#     count = a.checkperm(N, A, result)
#     print(count)