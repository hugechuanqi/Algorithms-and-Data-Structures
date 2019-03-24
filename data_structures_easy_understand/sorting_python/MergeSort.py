def MergeSort(A):

    length = len(A)

    if length <= 1 : return A

    n1 = int(length / 2)

    n2 = int(length - n1)

    L = []

    R = []

    for i in range(0, n1):

        L.append(A[i])

    for i in range(0, n2):

        R.append(A[n1 + i])

    if n1 > 1 : MergeSort(L)

    if n2 > 1 : MergeSort(R)

    i = 0

    j = 0

    for k in range(0, length):

        if L[i] < R[j]:

            A[k] = L[i]

            i = i + 1

            if i >= n1:

                for i in range(j, n2):

                    k = k + 1

                    A[k] = R[i]

                break

        else: 

            A[k] = R[j]

            j = j + 1

            if j >= n2:

                for j in range(i, n1):

                    k = k + 1

                    A[k] = L[j]

                break

    return A

a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]

print("排序前:", a)
a = MergeSort(a)
print("排序后：", a)
