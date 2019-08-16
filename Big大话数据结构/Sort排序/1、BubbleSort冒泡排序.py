class Solution:
    def BubbleSort(self, A):

        length = len(A)

        for i in range(0, length):

            for j in range(length - 1, i, -1):

                if A[j] < A[j - 1]:

                    (A[j], A[j - 1]) = (A[j - 1], A[j])

        return A

array = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]

print("冒泡排序前:", array)
a = Solution()
array_sort = a.BubbleSort(array)
print("冒泡排序后：", array_sort)