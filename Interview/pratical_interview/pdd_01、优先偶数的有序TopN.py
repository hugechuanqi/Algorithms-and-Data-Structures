## 题目：优先偶数的有序TopN
## 类型：

## 题目描述：偶数优先级>奇数优先级，数值大的优先级高。
## 核心：
## 思路：


import os
import sys
class Solution:
    def getTopNOfArr(self, Arr, N):
        Arr.sort(reverse=True)
        Even = [str(elem) for elem in Arr if elem%2==0]
        odd = [str(elem) for elem in Arr if elem%2!=0]
        Arr = Even+odd
        return Arr[:N]

if __name__ == "__main__":
    s, N = list(map(str, input().split(";")))
    N = int(N)
    Arr = list(map(int, s.split(",")))

    a = Solution()
    res = a.getTopNOfArr(Arr, N)
    print("TopN数为：", ','.join(res))

## 测试用例：
# 输入：
# 123,344,534;2
# 输出：
# 534,344

# 输入：
# 555503,772867,756893,339138,399447,40662,859037,628085,855723,974471,599631,636153,581541,174761,948135,411485,554033,858627,402833,546467,574367,360461,566480,755523,222921,164287,420256,40043,977167,543295,944841,917125,331763,188173,353275,175757,950417,284578,617621,546561,913416,258741,260569,630583,252845;10
# 输出：
# 913416,566480,420256,339138,284578,40662,977167,974471,950417,948135
