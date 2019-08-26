class Solution:
    def __init__(self):
        self.parent = lambda i : (i-1)/2
        self.left = lambda i : 2*i+1     #构建一个2*i+1的函数
        self.right = lambda i : 2*i+2
        self.exchange = lambda a,b : (b,a)

    def HeapAdjust(self, A, i, length):
        """ 构造大顶堆
        """
        l = self.left(i)     #中间根结点的左孩子(序号),i指该中间结点的序号
        r = self.right(i)    #中间根结点的右孩子（序号）
        if l < length and A[l]>A[i]:
            large = l
        else:
            large = i
        if r < length and A[r]>A[large]:
            large = r
        if large != i:
            (A[i], A[large]) = self.exchange(A[i], A[large])

            self.HeapAdjust(A, large, length)
        return A

    def HeapSort(self, A):
        length = len(A)
        
        # 构造大顶堆
        for i in range(int(length/2)-1, -1, -1):    # 从中间点length/2开始，到-1，逆序取值，因为int(length/2)处都是有孩子的结点
            self.HeapAdjust(A, i, length)

        # 从下往上，从左往右，将每个非终端结点（非叶结点）当做根结点，将其和子树调整成大顶堆
        for i in range(len(A) - 1, 0, -1):
            (A[0], A[i]) = self.exchange(A[0], A[i])    # 不断地将最大值放置顶部
            length = length -1
            self.HeapAdjust(A, 0, length)
        return A

if __name__ == "__main__":
    Arr = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]
    print("排序前：", Arr)
    a = Solution()
    a.HeapSort(Arr)
    print("排序后：", Arr)
