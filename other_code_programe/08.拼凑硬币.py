## 题目：拼凑硬币
## 类型：动态规划，递归，记忆搜索法

## 题目描述：小Q十分富有，拥有非常多的硬币，小Q拥有的硬币是有规律的，对于所有的非负整数K，小Q恰好各有两个面值为2^K的硬币，所以小Q拥有的硬币就是1,1,2,2,4,4,8,8,…。小Q有一天去商店购买东西需要支付n元钱，小Q想知道有多少种方案从他拥有的硬币中选取一些拼凑起来恰好是n元。

## 输入：输入包括一个整数n(1≤n≤10^18)，表示小Q需要支付多少钱。注意n的范围。
## 输出：输出一个整数，表示小Q可以拼凑出n元钱放的方案数。

# 核心：
# 思路：由于每个硬币的数量都是2个，因此当需要凑钱n元时，我们首先计算比n小的2的指数次的值，即为一个硬币值，然后将剩余的需要凑的钱n-2*m递归计算出剩余的硬币数。

## 一般递归法
def get_num(n):
    if n in mem:
        return mem[n]
    else:
        m = int(math.log2(n))
        ans = get_num(n - 2**m) + get_num(2**(m+1) - 2 - n)
        #  get_num(n - 2**m)表示只用一个可以使用的最大的硬币， get_num(2**(m+1) - 2 - n) = get_num((2**m-1)*2 - n)，其中 (2**m-1)*2 表示不使用最大的硬币时，余下的硬币所能表示的最大值，(2**m-1)*2-n表示需要剔除的硬币的拼凑方法数==使用余下硬币拼凑n的方法数（正难则反）
        mem[n] = ans
        return ans

## 记忆搜索法
def get_num2(n, mem):
    if n in mem:
        return mem[n]
    count = 0
    if ((n&1) != 1):    # n为偶数
        count = get_num2(n>>1, mem) + get_num2((n>>1) -1, mem)
    else:
        count = get_num2(n>>1, mem)
    mem[n] = count
    return count

import sys
import math
n = int(sys.stdin.readline())
mem = {-1:0, 0:1, 1:1}
print(get_num2(n, mem))
print(mem)

## 测试用例：
# 输入：
# 6
# 输出：
# 3
