## 题目：堆排序（求TopK）
## 类型：排序

## 题目描述：将数组或者某个数据表以某关键字进行堆排序。
## 思路：首先将待排序的序列构造成一个大顶堆。此时，整个序列的最大值就是堆顶的根结点。将它移走（其实就是将其与堆数组的末尾元素交换，此时末尾元素就是最大值），然后将剩余的n-1个序列重新构造一个大顶堆，这样就会得到n个元素地次大值。如此反复循环，就能得到一个有序序列。

## 注意：构建的大顶堆和小顶堆是按照层序遍历的方式进行的。

class Solution:
    def __init__(self):
        self.parent = lambda i : (i-1)/2
        self.left = lambda i : 2*i+1     #构建一个2*i+1的函数
        self.right = lambda i : 2*i+2
        self.exchange = lambda a,b : (b,a)

    def HeapAdjust(self, Arr, i, length):
        """ 构造大顶堆
        """
        l = self.left(i)     #中间根结点的左孩子(序号),i指该中间结点的序号
        r = self.right(i)    #中间根结点的右孩子（序号）
        if l < length and Arr[l]>Arr[i]:
            large = l
        else:
            large = i
        if r < length and Arr[r]>Arr[large]:
            large = r
        if large != i:
            (Arr[i], Arr[large]) = self.exchange(Arr[i], Arr[large])

            self.HeapAdjust(Arr, large, length)     # 在较大值的孩子结点中继续进行堆调整
        return Arr

    def HeapSort(self, Arr):
        """ 堆排序
        """
        length = len(Arr)
        
        # 构造大顶堆
        for i in range(int(length/2)-1, -1, -1):    # 从中间点length/2开始，到-1，逆序取值，因为int(length/2)处都是有孩子的结点
            self.HeapAdjust(Arr, i, length)

        # 从下往上，从左往右，将每个非终端结点（非叶结点）当做根结点，将其和子树调整成大顶堆
        for i in range(len(Arr) - 1, 0, -1):
            (Arr[0], Arr[i]) = self.exchange(Arr[0], Arr[i])    # 不断地将最大值放置顶部
            length = length -1
            self.HeapAdjust(Arr, 0, length)
        return Arr

if __name__ == "__main__":
    Arr = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]
    print("排序前：", Arr)
    a = Solution()
    a.HeapSort(Arr)
    print("排序后：", Arr)
