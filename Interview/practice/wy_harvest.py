#丰收
#难点：如何进行比较

n = list(map(int, input().split()))[0]
a = list(map(int, input().split()))
m = list(map(int, input().split()))[0]
q = list(map(int, input().split()))
# print(n, a, m, q)

max_value = [0]*n
for i in range(n):
    if i==0:
        max_value[i] = a[i]
    else:
        max_value[i] = max_value[i-1]+a[i]
# print(max_value)

for j in range(m):
    l, r = 0, n-1
    while(l<r):
        mid = int((l+r)/2)
        if q[j] <= max_value[mid]:
            r = mid+1
        else:
            l = mid
    print(r+1)

## 测试用例
#输入：
#5
#2 7 3 4 9
#3
#1 25 11
#输出：
#1
#5
#3
