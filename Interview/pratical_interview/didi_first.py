# import sys
# n = sys.stdin.readline().strip()
# n = int(n)
# a = []
# a = sys.stdin.readline().strip()
# a = list(eval(a))
# b = []
# b = sys.stdin.readline().strip()
# b = list(eval(b))

import numpy as np
n = input()
n = int(n)
a = input()
a = list(map(int, a.split()))

b = input()
b = list(map(int, b.split()))

print(a)
a = np.sort(a)
b = np.sort(b)

S=0
if(n<=50 and 0<=a[n-1]<=100 and 0<=b[n-1]<=100):
    for i in range(n):
        temp = a[i]*b[n-1-i]
        S = S + temp

print(S)
