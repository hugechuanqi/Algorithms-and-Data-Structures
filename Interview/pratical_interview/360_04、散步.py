## 题目：散步
## 类型：递归判断

## 题目描述：小明在数轴上行走，不知道起点和每一次行走之后的位置，只知道每次行走了多长距离，距离从小明每次看手环开始，给出数轴大小N，给出总共看手环的次数M，并给出每次看手环时对应的行走距离Di，要求计算出可能的起始点。
## 输入：
# 10 3
# 5
# 2
# 6
## 输出：
# 8

## 思路：假设从每一个起点出发，判断每次是否能行走给定的距离，如果能全部完成行走的距离，则为可能的起点（此题还是存在一些问题）


def isOK(i,N,k):
    if i<1 or i>N:
        return False
    if k>=len(num):
        return True
    return isOK(i+num[k],N,k+1) or isOK(i-num[k],N,k+1)

if __name__ == "__main__":
    N,M = list(map(int,input().split()))
    num = []
    for _ in range(M):
        num.insert(0,int(input()))

    res = 0
    for i in range(1,N+1):
        if isOK(i,N,0):
            res += 1
    print(res)

