## 从薯片两端选取快乐值，求小米是否能获得最大值
# class Solution:
#     def checkWin(self, Arr):
#         xm_count, dm_count = 0, 0
#         low = 0
#         high = len(Arr)-1
#         i = 1
#         while(low<=high):
#             if i%2==0:  # 小米取i%2==0
#                 if Arr[low]<Arr[high]:
#                     dm_count += Arr[high]
#                     high -= 1
#                 else:
#                     dm_count += Arr[low]
#                     low += 1
#             if i%2!=0:  # 大米取i%2!=0
#                 if Arr[low]<Arr[high]:
#                     xm_count += Arr[high]
#                     high -= 1
#                 else:
#                     xm_count += Arr[low]
#                     low += 1
#             i += 1
#         if xm_count >= dm_count:
#             return True
#         else:
#             return False

# if __name__ == "__main__":
#     Arr = list(map(int, input().split()))
#     a = Solution()
#     if a.checkWin(Arr):
#         print("Yes")
#     else:
#         print("No")

## 测试用例：
# 输入：
# 1 4 2
# 输出：
# No

def checkWin(Arr):
    length = len(Arr)
    dp = [[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        if length%2 == 0:
            dp[i][i] = -Arr[i]      # 对角线
        else:
            dp[i][i] = Arr[i]
    for s in range(1, len(Arr)):
        for i in range(len(Arr) - s):
            j = i + s
            dp[i][j] = max(dp[i][i] - dp[i+1][j], dp[j][j]-dp[i][j-1])

    return dp

if __name__ == "__main__":
    Arr = list(map(int, input().split()))
    left_num = sum(Arr)
    dp = checkWin(Arr)

    if len(Arr) % 2 == 1:
        print("Yes") if dp[0][len(Arr)-1] >= 0 else print("No")
    if len(Arr) % 2 == 0:
        print("Yes") if dp[0][len(Arr)-1] <= 0 else print("Yes")

## 测试用例：
# 输入：
# 1 4 2
# 输出：
# No
