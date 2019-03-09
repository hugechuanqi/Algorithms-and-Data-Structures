def BubbleSort(A):

    length = len(A)

    for i in range(0, length):

        for j in range(length - 1, i, -1):

            if A[j] < A[j - 1]:

                (A[j], A[j - 1]) = (A[j - 1], A[j])

    return A

a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]

print("排序前:", a)
a = BubbleSort(a)
print("排序后：", a)