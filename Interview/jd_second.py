# coding:utf-8
## 还原————即哪些数字可以为0，并且满足三个条件
# 1.    a_1<=a_2
# 2.    a_n<=a_(n-1) （此时n>2）
# 3.    a_i<=max(a_{i-1},a_{i+1})
# 但是很不幸的是，在序列保存的过程中，有些数字丢失了，
# 请你根据上述条件，计算可能有多少种不同的序列可以满足以上条件。
import sys
length = int(input("请输入序列长度"))
a = [0]*length
for i in range(length):
    a[i] = int(input("请输入序列的每个非负整数"))
a_pop=[]
for i in range(length):
    if a[i]==0:
        a_pop.append(i)
for i in range(len(a_pop)):
    a.pop(a_pop[i])

L = len(a)

number=0
if L==2:
    if a[0]<a[1]:
        number = number+1
if L>2:
    for i in range(L):
        if i<L-1:
            if a[0]<a[1] and a[i]>=a[i+1] and a[i] <= max(a[i-1], a[i+1]):
                number = number+1
        else:
            if a[0]<a[1] and a[i-1]>=a[i] and a[i-1] <= max(a[i-2], a[i]):
                number = number+1

sys.stdout.write(str(number))


