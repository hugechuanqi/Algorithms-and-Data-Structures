# # 标准的链表结点定义
# class LNode:
#     def __init__(self, elem, next_=None):
#         self.elem = elem
#         self.next = next_

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
    def FindKthToTail(self, head, k):
        if not head or k<=0:
            return None
        q = head
        p = head
        for i in range(k-1):    # 先走K-1步，不能走K步，因为q指向第一个结点，假设链表长度为K，走k步就为空了，但实际上第一个结点就为倒数第K个结点
            if q.next is not None:
                q = q.next
            else:
                return None     # 如果整个链表的长度比K小，则输出为空
        while(q.next is not None):
            p = p.next
            q = q.next
        return p

if __name__ == "__main__":
    ## 测试用例
    s = [1, 2, 3,  4, 5]
    LL = LinkList()
    head = LL.buildList(s)
    print("链表为：", LL.printLinkList(head))

    a = Solution()
    k = 2
    node = a.FindKthToTail(head, k)
    print("倒数第",k,"个结点为：", node.val)

