def InsertSort(A):

    for i in range(1, len(A)):

        key = A[i]

        j = i - 1

        while (j >= 0) and (A[j] > key):

            A[j + 1] = A[j]

            j = j - 1

        A[j+1] = key

    return A

a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]

print("排序前:", a)
a = InsertSort(a)
print("排序后：", a)