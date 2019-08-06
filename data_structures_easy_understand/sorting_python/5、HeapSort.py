parent = lambda i : (i-1)/2
left = lambda i : 2*i+1     #构建一个2*i+1的函数
right = lambda i : 2*i+2
exchange = lambda a,b : (b,a)

def HeapAdjust(A, i, length):
    l = left(i)     #中间根结点的左孩子(序号),i指该中间结点的序号
    r = right(i)    #中间根结点的右孩子（序号）
    if l < length and A[l]>A[i]:
        large = l
    else:
        large = i
    if r < length and A[r]>A[large]:
        large = r
    if large != i:
        (A[i], A[large]) = exchange(A[i], A[large])

        HeapAdjust(A, large, length)
    return A

def HeapSort(A):
    length = len(A)
    
    # 构造大顶堆
    for i in range(int(length/2)-1, -1, -1):    # 从中间点length/2开始，到-1，逆序取值
        HeapAdjust(A, i, length)

    # 从下往上，从左往右，将每个非终端结点（非叶结点）当做根结点，将其和子树调整成大顶堆
    for i in range(len(A) - 1, 0, -1):
        (A[0], A[i]) = exchange(A[0], A[i])
        length = length -1
        HeapAdjust(A, 0, length)
    return A


a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]
print("排序前：",a)
a = HeapSort(a)
print("排序后：", a)