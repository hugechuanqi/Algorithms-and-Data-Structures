## 题目：复读

def checkSubs(str1, str2, interval):
    length0 = len(str1)
    i = 0
    while(length0>=interval*(i+1)):
        if str1[i*interval:interval*(i+1)]!=str2[i*interval:interval*(i+1)]:
            return False
        i = i + 1
    str11 = str1[i*interval:]
    str22 = str2[i*interval:]
    for j in range(len(str11)):
        if str11[j] != str22[j]:
            return False
    return True

if __name__ == "__main__":
    length = int(input())
    str1 = input()
    m = int(input())
    count = 0
    for i in range(m):
        str2 = input()
        interval = len(str2)
        a = length//interval
        b = length%interval
        if b!=0:
            a = a+1
        if checkSubs(str1, str2*a, interval):
            count += 1
    print(count)


## 测试用例：
# 输入：
# 9
# abaabaaba
# 3
# aba
# ab
# abaaba
# 输出：
# 2

# 输入：
# 30
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# 10
# aaaaaa
# aaaa
# aaaaaaaaaaaaa
# aaaaaa
# a
# aaaaaaaaaaab
# bbbaaa
# aababa
# avavavavav
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaab
# 输出：
# 5