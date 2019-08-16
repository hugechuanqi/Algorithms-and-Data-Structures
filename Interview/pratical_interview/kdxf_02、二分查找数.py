
def findNumber(array, data):
    n = len(array)
    if n<1:
        return False
    mid = n//2
    print(n, mid)
    if array[mid]>data:
        return findNumber(array[0:mid], data)
    elif array[mid]<data:
        return findNumber(array[mid+1:], data)
    else:
        return True

n = int(input())
array = list(map(int, input().split()))
data = int(input())
if findNumber(array, data):
    print(array.index(data))
else:
    print("-1")


## 测试用例：
# 输入：
# 6
# 7 13 15 17 19 21
# 19
# 输出：
# 4
