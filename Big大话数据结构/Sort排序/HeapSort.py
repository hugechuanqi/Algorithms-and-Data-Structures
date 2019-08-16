parent = lambda i : (i -  1) / 2

left = lambda i : 2 * i + 1

right = lambda i : 2 * i + 2

exchange = lambda a, b : (b, a)

def maxHeapfy(A, i, length):

    l = left(i)

    r = right(i)

    if l < length and A[l] > A[i]:

        large = l

    else:

        large = i

    if r < length and A[r] > A[i]:

        large = r

    if large != i:

        (A[i], A[large]) = exchange(A[i], A[large])

        maxHeapfy(A, large, length)

    return A

def buildHeap(A, length):

    for i in range(int(length / 2) - 1, -1, -1):

        maxHeapfy(A, i, length)

def HeapSort(A):

    length = len(A)

    buildHeap(A, length)

    for i in range(len(A) - 1, 0, -1):

        (A[0], A[i]) = exchange(A[0], A[i])

        length = length - 1

        maxHeapfy(A, 0, length)

    return A

a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]

print("排序前:", a)
a = HeapSort(a)
print("排序后：", a)