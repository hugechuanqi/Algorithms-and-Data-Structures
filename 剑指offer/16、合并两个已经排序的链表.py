## 题目：合并两个已经排序的链表
## 类型：链表，合并

## 题目描述：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

## 输入：
# [1,3,5,7,9]
# [2,4,6,8,10] 
## 输出：
# [1,2,3,4,5,6,7,8,9,10]

# 核心：利用两个指针分别取值比较，中止条件为1个为空，1个不为空，之后再将不为空的剩余链表添加至融合链表后。
# 思路：首先建立两个指针p,q，分别指向两个链表的头节点，然后比较p,q取值大小，较小的链表节点添加到新的融合链表中，并将较小节点对应指针后移一位，指向下一个节点，较大取值节点指针不变，依次比较，直到两个指针有一个为空，然后将不为空的链表直接添加至融合链表中。

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class List:
    def buildList(self, Arr):
        """ 建立链表
        """
        head = ListNode(Arr[0])
        p = head
        for i in range(1, len(Arr)):
            p.next = ListNode(Arr[i])
            p = p.next
        p.next = None
        return head

class Solution:
    def Merge(self, pHead1, pHead2):
        """ 合并两个已经排序的链表到一个链表中
        """
        pMerge = ListNode(0)
        p = pMerge
        while(pHead1 and pHead2):   # 循环条件为里那个指针都不为空
            if pHead1.val<pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next
             
        if not pHead1:  # 假设pHead1为空，则pHead2必然还有值
            p.next = pHead2
        else:                      # 假设pHead2为空，则pHead1必然还有值
            p.next = pHead1
        return pMerge.next

if __name__ == "__main__":
    Arr1 = [1,3,5,7,9]
    Arr2 = [2,4,6,8,10]
    a = List() 
    pHead1 = a.buildList(Arr1)
    pHead2 = a.buildList(Arr2)
    
    b = Solution()
    pMerge = b.Merge(pHead1, pHead2)
    p = pMerge
    while(p):
        print(p.val)
        p = p.next

## 测试用例：
# 输入：
# [1,3,5,7,9]
# 输出：
# [2,4,6,8,10]
