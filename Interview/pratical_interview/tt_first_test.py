#头条第一道面试
M1 = [1,4,16,64]
M2 = 1024

def money(money1, money2, shop):
    remain = money2 - shop
    i3 = 0
    i2 = 0
    i1 = 0
    i0 = 0
    while(remain>=64):
        remain = remain - money1[3]
        i3 = i3 + 1
    while(remain>=16):
        remain = remain - money1[2]
        i2 = i2 + 1
    while(remain>=4):
        remain = remain - money1[1]
        i1 = i1 + 1
    while(remain>=1):
        remain = remain - money1[0]
        i0 = i0 + 1
    return i3+i2+i1+i0

N = input()
print(money(M1, M2, int(N)))

