def getNewArr(xs, k):
    res = []
    for low in range(0, len(xs)-k+1):
        high = low+(k-1)
        average = sum(xs[low:high+1])/k
        average = round(average, 2)
        res.append(str(average))
    return res

if __name__ == "__main__":
    xs = list(map(int, input().split()))
    k = int(input())
    res = getNewArr(xs, k)
    print(' '.join(res))

## 测试用例：
# 输入：
# 1 2 3 4 5 6 7
# 3
# 输出：
# 2.00 3.00 4.00 5.00 6.00