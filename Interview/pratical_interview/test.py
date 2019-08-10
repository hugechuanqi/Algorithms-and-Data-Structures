#!/bin/python
# -*- coding: utf8 -*-
def  GetResult(K):
    flag = True
    n = 1
    while(flag==True):
        # print(n)
        if n == 1 and 1>K:
            return n
        if n==2 and 2 + 1 > K*2:
            return n
        totalValue = 1
        nb = n
        while(nb>0):
            totalValue = totalValue*nb
            nb -= 1
        sumValue = 0
        for i in range(1,n+1):
            sumValue = sumValue + totalValue//i
        if sumValue > K*totalValue:
            flag = False
            return n
        n += 1

K = int(input())
res = GetResult(K)
print(res, "\n")