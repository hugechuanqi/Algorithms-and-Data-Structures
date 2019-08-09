## 题目：彩色宝石项链
## 类型：队列

while True:
    try:
        s = input()
        l = len(s)
        min_ = l
        for i in range(l):
            x = []
            for j in "ABCDE":
                x.append(s.find(j))
            x.sort()
            if min_ > x[-1]:
                min_ = x[-1]
            s = s[1:] + s[0]
        print(l - min_ -1)
    except:
        break



