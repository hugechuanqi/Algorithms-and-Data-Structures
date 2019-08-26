## 题目：丰收
## 类型：数组，查找

## 题目描述：在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
## 输入：
# 第一行一个数n(1 <= n <= 105)。
# 第二行n个数ai(1 <= ai <= 1000)，表示从左往右数第i堆有多少苹果
# 第三行一个数m(1 <= m <= 105)，表示有m次询问。
# 第四行m个数qi，表示小易希望知道第qi个苹果属于哪一堆。
## 输出：
# m行，第i行输出第qi个苹果属于哪一堆。

## 核心难点：如何比较询问的苹果和已有的苹果。
## 思路：获取每一堆的最大值，建立一个最大值区间，判断询问的苹果输入哪一个范围内。区间查找可以用二分法，因此此题主要考察二分查找。

class Solution:
    def getIndex(self, n, a, m, q):
        max_value = [0]*n
        for i in range(n):  #建立每堆苹果的最大值区间
            if i==0:
                max_value[i] = a[i]
            else:
                max_value[i] = max_value[i-1]+a[i]
        # print(max_value)
        for j in range(m):
            l, r = 0, n-1
            while(l+1!=r):     # 二分法查找
                mid = int((l+r)/2)
                if q[j] <= max_value[mid]:
                    r = mid
                elif q[j] > max_value[mid]:
                    l = mid
            print(r+1 if q[j]>max_value[l] else l+1)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    aa = Solution()
    aa.getIndex(n, a, m, q)

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
