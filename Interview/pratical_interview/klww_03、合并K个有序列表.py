## 题目：合并K个有序列表
## 类型：链表

## 题目描述：合并K个有序列表
## 思路：首先将K个有序列表看作K-1个两两成对的有序列表。对于每对有序列表，新建一个合并列表，利用双指针分别指向两个列表的头部，然后顺序比较，依次排序取出。

def getSortArray(array):
    res = []
    for item in array:
        res.extend(item)
    return sorted(res)

def MergeSort(nums):
    #请牢记传入的参数是多维数组
    #此处是递归结束条件
    if len(nums) <= 1:
        return nums
    #取中间位置 
    mid = len(nums) // 2
    
    #此处实现递归
    #记住此处得到的也是多维数组
    Left = MergeSort(nums[:mid])
    
    Right = MergeSort(nums[mid:])

    #print(Left[0], Right[0])
    #要传入的参数是数组中第一个索引处的值
    return Sort_list(Left[0], Right[0])

def Sort_list(Left, Right):
    #存储排序后的值
    res = []
    a = 0
    b = 0

    while a < len(Left) and b < len(Right):
 
        if Left[a] < Right[b]:
            res.append(Left[a])
            a += 1
        else:
            res.append(Right[b])
            b += 1
    #因为存在一个到终点后，另一个还没到终点
    #这时就需要将没到终点的剩下的值添加到数组中
    while a < len(Left):
        res.append(Left[a])
        a += 1

    while b < len(Right):
        res.append(Right[b])
        b += 1
    #将一维数组二维化
    res = [res]

    return res

if __name__ == "__main__":
    K = int(input())
    array = [[0]]*K
    for i in range(K):
        temp = list(map(int, input().split(",")))
        array[i] = temp
    res = getSortArray(array)
    # res = MergeSort(array)
    res = ''.join(str(x) for x in res[0])  if res else '0'
    print(",".join(res))

## 测试用例：
# 输入：
# 3
# 1,4
# 1,3,4
# 2,6
# 输出：
# 1,1,2,3,4,4,6
