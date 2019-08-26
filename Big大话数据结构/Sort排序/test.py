class Solution:
    def __init__(self):
        self.left = lambda i:2*i+1
    def HeapAdjust(self, A, i, length):
        l = self.left(i)

    def HeapSort(self, A):
        length = len(A)
        for i in range(int(length/2)-1, -1, -1):
            self.HeapSort(A, i, length)

        for i in range(len(A)-1, 0, -1):
            (A[0], A[i]) = (A[i], A[0])
            length = length-1
            self.HeapAdjust(A, 0, length)
        return A

if __name__ == "__main__":
    Arr = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]
    print("排序前", Arr)
    a = Solution()
    a.HeapSort(Arr)
    print("排序后", Arr)

