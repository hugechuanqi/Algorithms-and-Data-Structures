# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        pPre = ListNode(None)
        pPre.next = pHead
        head = pPre
        pNode = pHead
        while(pNode is not None):
            
            pNext = pNode.next
            duplicated = False
            if pNext is not None and pNode.val == pNext.val:
                duplicated = True

            if not duplicated:
                print("not duplicated", pNode.val)
                pPre = pNode
                pNode = pNext
            else:
                # 删除方式
                value = pNode.val
                while(pNode is not None and pNode.val == value):
                    print("duplicated", pNode.val)
                    pNode = pNext
                    pNext = pNode.next
                # 串联链表
                if not pPre:
                    pPre = pNode
                else:
                    pPre.next = pNode
        return head.next

class Solution2:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        pPre = ListNode(None)
        pNode = pHead
        pPre.next = pNode
        duplicated_flag = False
        while(pNode is not None and pNode.next is not None):
            pNext = pNode.next
            if pNode.val == pNext.val:
                duplicated_flag = True
                pNode.next = pNext.next
                pNext =None
            elif duplicated_flag:
                pPre.next = pNode.next
                pNode = pNode.next
                duplicated_flag = False
            else:
                print("ok")
                pPre = pNode
                pNode = pNode.next
        
        if duplicated_flag:
            pPre.next = None
        return pPre

## 测试用例
s = [1, 1, 2, 3, 3, 4, 4, 5,6,7,8]
# s = [1,1,1,1,1,2]
listNode = ListNode(list(s)[0])
p = listNode
i = 0
for elem in s:
    if i != 0:
        p.next = ListNode(elem)
        p = p.next
    i = i + 1
    print("load to listNode:", p.val)

print("删除前链表为：")
p = listNode
while( p is not None):
    print(p.val)
    p = p.next

a = Solution2()
p = listNode
pHead = a.deleteDuplication(p)      #这样能保证链表头还是listNode指向的结点，但是整个链表结构会发生改变
print("删除重复结点后链表为：")
while(pHead is not None):
    print(pHead.val)
    pHead = pHead.next


# class Solution3:
#     def deleteDuplication(self, pHead):
#         # write code here
#         if not pHead:
#             return None
#         preNode=ListNode(None)
#         preNode.next=pHead
#         head=preNode
#         flg=False
#         while pHead and pHead.next:
#             pNext=pHead.next
#             if pHead.val==pNext.val:
#                 flg=True
#                 pHead.next=pNext.next
#                 pNext.next=None
#             elif flg==True:
#                 preNode.next=pHead.next
#                 pHead=pHead.next
#                 flg=False
#             else:
#                 preNode=pHead
#                 pHead=pHead.next
#         if flg:
#             preNode.next=None
#         return preNode