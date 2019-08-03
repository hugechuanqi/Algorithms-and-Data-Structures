# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None

        pPre = None
        pNode = pHead
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
node = a.ReverseList(listNode)
print(node, node.val)

# a2 = Solution2()
# node2 = a2.ReverseList(listNode)
# print(node2, node2.val)
