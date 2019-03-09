def partition(A, p, r):

    x = A[r]

    i = p - 1

    for j in range(p, r):

        if A[j] <= x:

            i = i + 1

            (A[i], A[j]) = (A[j], A[i])

    (A[i + 1], A[r]) = (A[r], A[i + 1])

    return i + 1

def QuickSort(A, p, r):

    if p < r:

        q = partition(A, p, r)

        QuickSort(A, p, q - 1)

        QuickSort(A, q + 1, r)

    return A

a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]

print("排序前:", a)
a = QuickSort(a, 0, len(a) - 1)
print("排序后：", a)