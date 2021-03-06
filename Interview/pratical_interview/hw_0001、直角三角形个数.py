## 题目：直角三角形个数
## 类型：数学公式

## 题目描述：给出三角形的周长p，要求求出可能的直角三角形个数
## 核心：1、可以用三层循环判断；2、可以借助直接三角形的欧拉公式使用两层循环判断；3、可以根据每个变量的大小缩小循环路径；4、可以借助周长公式+欧拉公式+变量范围使用一层循环判断。（实际应用中循环越少越好，并且不同要求可能公式不一样）
## 思路：根据数学公式，由i+k+j=l，i**2 + j**2 = k**2，可以解得j = l - l**2/(2l-2i)，其中l为周长，0<i<=j<k（直接将k代入求解即可）

class Solution:
    def getNum(self, p):
        ans = 0
        for i in range(1, int(p/3)):
            j = p - p*p/(2*p-2*i)
            if i < j and j -int(j)<0.00001:
                ans += 1
        return ans

if __name__ == "__main__":
    p = int(input())
    a = Solution()
    res = a.getNum(p)
    print(res)

## 测试用例：
# 输入：
# p=120
# 输出：
# 3