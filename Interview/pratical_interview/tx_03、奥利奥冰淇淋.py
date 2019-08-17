## 时间复杂度超了，40%
def getNumber(n, m, w, v):
    money = 0
    num = 0
    while(money<=m):
        print(n, m, w, v)
        money = 0
        ## 是否存在0
        for i in range(n):
            if w[i]>0:
                w[i] = w[i] - 1
            else:
                money += v[i]
        if money==0:
            num += 1
        elif money<=m:
            m = m - money
            num += 1
        else:
            break
    return num

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    w = list(map(int, input().split()))
    v = list(map(int, input().split()))
    num = getNumber(n, m, w, v)
    print(num)