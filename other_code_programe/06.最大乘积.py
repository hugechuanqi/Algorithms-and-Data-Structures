## 给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1) 

## 第一种方法
# print("请输入无序数组长度：")
# L = int(input())
# print("请输入数组的各个元素(必须以空格分开)：")
# arr = input()
# arr = list(map(int, arr.strip().split()))
# arr.sort()

# firstValue = arr[-1]*arr[-2]*arr[-3]      #如果出现数组越界，原因可能是变量名称太长（系统问题），firstValue改为fr即可
# secondValue = arr[-1]*arr[0]*arr[1]

# if firstValue>secondValue:
#     print(firstValue)
# if firstValue<=secondValue:
#     print(secondValue)


## 第二种方法
print("请输入无序数组长度：")
n = int(input())
print("请输入数组的各个元素(必须以空格分开)：")
arr = list(map(int, input().strip().split()))
# arr = [int(i) for i in arr.strip().split()]

def maxProduct(n, arr):
    if n<3:
        return None
    if n==3:
        return arr[0]*arr[1]*arr[2]
    a,b = [],[]
    a1,a2 = arr[:],arr[:]
    for i in range(3):
        max1 = max(a1)
        a.append(max1)
        a1.remove(max1)
    for i in range(2):
        min2 = min(a2)
        b.append(min2)
        a2.remove(min2)
    maxValue = max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])
    return maxValue

print(maxProduct(n,arr))
