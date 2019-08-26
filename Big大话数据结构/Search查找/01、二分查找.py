# coding: utf-8
## 扩展：二分法只能查找排序好的数组，那如何利用非遍历的方法查找未排序的数组呢？假设数组中存储的是字符串，又该如何？

class Solution:
    # 递归版（如果找到，则直接返回list_[mid]）
    def binary_lookup(self, list_, key):
        n = len(list_)
        if n<1:
            return False
        mid = n//2
        if list_[mid] < key:
            return self.binary_lookup(list_[mid+1:], key)
        elif list_[mid] > key:
            return self.binary_lookup(list_[0:mid], key)
        else:
            return True

    # 非递归版（如果找到，则直接返回mid，mid即位置）
    def binary_lookup(self, list_, key):
        n = len(list_)
        low = 0
        high = n-1
        while(low<high):    # 正好找到，因此是low<high，如果确定在某个区间，则是low+1<high，因为基本上找不到low=high
            mid = (low+high)//2
            if list_[mid] < key:
                low = mid
            elif list_[mid] > key:
                high = mid
            else:
                return True
        return False

if __name__ == "__main__":
    # array = list(map(int, input().split()))
    # key = int(input())
    array = [7, 9, 11, 13, 15, 17]
    key =  15
    a = Solution()
    if a.binary_lookup(array, key):
        print(array.index(key))
    else:
        print("-1")


## 测试用例：
# 输入：
# 7 9 11 13 15 17
# 15
# 输出：
# 5
