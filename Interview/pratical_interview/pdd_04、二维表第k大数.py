## 题目：
## 类型：

## 题目描述：
## 核心：
## 思路：


def getKnum(n,m,k):
    res = []
    for i in range(n):
        for j in range(m):
            tmp = (i+1)*(j+1)
            res.append(tmp)
    res = sorted(res)
    return res[-k]


if __name__ == "__main__":
    n,m,k = list(map(int, input().split()))
    res = getKnum(n,m,k)
    print(res)
