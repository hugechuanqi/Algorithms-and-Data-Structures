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

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k<=0:
            return None
        q = head
        p = head
        for i in range(k-1):
            if q.next is not None:
                q = q.next
            else:
                return None
        # print("p结点数据域：", p.val, "，q结点数据域：", q.val)
        while(q.next is not None):
            p = p.next
            q = q.next
        return p

## 测试用例
s = {1, 2, 3,  4, 5}
listNode = ListNode(list(s)[0])
p = listNode
i = 0
for elem in s:
    if i != 0:
        p.next = ListNode(elem)
        p = p.next
    i = i + 1

a = Solution()
node = a.FindKthToTail(listNode, 2)
print(node.val, node.next)

