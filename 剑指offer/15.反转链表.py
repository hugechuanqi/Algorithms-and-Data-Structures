# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
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

    def printLinkList(self, head):
        """ 从头到尾打印链表
        """
        p = head
        result = []
        while(p):
            result.append(p.val)
            p = p.next
        return result

class Solution:
   """  翻转链表"""
    def ReverseList(self, pHead):
        """ 三指针法
        """
        if not pHead:
            return None

        pPre = None
        pNode = pHead   # 表示当前结点
        pReversedHead = None
        while(pNode is not None):
            pNext = pNode.next
            if pNode.next is None:
                pReversedHead = pNode
            pNode.next = pPre
            pPre = pNode
            pNode = pNext
        
        return pReversedHead

# ## 方法二
# class Solution2:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         # write code here
#         if not pHead or not pHead.next:
#             return pHead

#         pPre = None
#         pNode = pHead
#         while(pNode is not None):
#             pNext = pNode.next
#             pNode.next = pPre
#             pPre = pNode
#             pNode = pNext
        
#         return pPre

if __name__ == "__main__":
    ## 测试用例
    s = [1, 2, 3,  4, 5]
    LL = LinkList()
    head = LL.buildList(s)
    print("链表为：", LL.printLinkList(head))

    a = Solution()
    node = a.ReverseList(head)
    print("翻转链表为：", LL.printLinkList(node))

# a2 = Solution2()
# node2 = a2.ReverseList(listNode)
# print(node2, node2.val)
