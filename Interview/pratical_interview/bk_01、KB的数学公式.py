#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************

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




#******************************结束写代码******************************


_K = int(input())

res = GetResult(_K)

print(res , "\n")