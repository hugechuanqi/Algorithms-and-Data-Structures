## 题目：拼凑硬币
## 类型：动态规划

## 要求：小Q十分富有，拥有非常多的硬币，小Q拥有的硬币是有规律的，对于所有的非负整数K，小Q恰好各有两个面值为2^K的硬币，所以小Q拥有的硬币就是1,1,2,2,4,4,8,8,…。小Q有一天去商店购买东西需要支付n元钱，小Q想知道有多少种方案从他拥有的硬币中选取一些拼凑起来恰好是n元。

## 输入：输入包括一个整数n(1≤n≤10^18)，表示小Q需要支付多少钱。注意n的范围。
## 输出：输出一个整数，表示小Q可以拼凑出n元钱放的方案数。


import sys
import math
n = int(sys.stdin.readline())
mem = {-1:0, 0:1, 1:1}

def get_num(n):
    if n in mem:
        return mem[n]
    else:
        m = int(math.log2(n))
        ans = get_num(n - 2**m) + get_num(2**(m+1) - 2 - n)
        mem[n] = ans
        return ans

print(get_num(n))
