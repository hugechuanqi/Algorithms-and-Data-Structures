# coding:utf-8
# n = int(input())
# m = int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# k_max = max(a)+m
# for i in range(m):
#     index_min = a.index(min(a))
#     a[index_min]+=1
# k_min = min(a)
# print(k_min,k_max)

# 已通过
n = int(input())
m = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
k_max = max(a)+m
for i in range(m):
    index_min = a.index(min(a))
    a[index_min]+=1
k_min = max(a)
print(k_min,k_max)