
## 题目描述：只能买连续相邻的手办
def getNum(S, Arr):
    for size in range(1, len(Arr)+1):
        for low in range(len(Arr)):
            high = low+(size-1)
            tmp = Arr[low:high+1]
            if sum(tmp)>S:
                return size
    return -1

if __name__ == "__main__":
    N, S = list(map(int, input().split()))
    Arr = list(map(int, input().split()))
    count = getNum(S, Arr)
    print(count)

## 测试用例：
# 输入：
# 5 7
# 1 2 3 4 5
# 输出：
# 2

# 输入：
# 5 16
# 1 2 3 4 5
# 输出：
# 2


# def getNum(S, Arr):
#     Arr.sort(reverse=True)
#     count = 0
#     for price in Arr:
#         if price<=S:
#             count += 1
#             S = S - price
#     if S>0:
#         return -1
#     return count

# if __name__ == "__main__":
#     N, S = list(map(int, input().split()))
#     Arr = list(map(int, input().split()))
#     count = getNum(S, Arr)
#     print(count)