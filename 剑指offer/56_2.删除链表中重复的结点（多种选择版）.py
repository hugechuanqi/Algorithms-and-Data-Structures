# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        flag = 0    #flag = 0表示删除所有的重复结点，flag = 1表示保留重复结点的最后一个结点，删除其他结点，flag=2表示保留重复结点的第一个结点，删除其他结点
        if not pHead:
            return None
        pPre = ListNode(None)
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
                if flag==0:     
                    value = pNode.val
                    while(pNode is not None and pNode.val == value):
                        print("duplicated", pNode.val)
                        pNode = pNext
                        pNext = pNode.next
                elif flag==1:
                    pNode = pNext
                elif flag==2:
                    pHold = pNode
                    value = pNode.val
                    while(pNode is not None and pNode.val == value):
                        print("duplicated",pNode.val)
                        pNext = pNode.next
                        pNode = pNext
                    pHold.next = pNode
                    pNode = pHold
                # 串联链表
                if not pPre:
                    pPre = pNode
                else:
                    pPre.next = pNode
        return pHead

## 测试用例
s = [1, 1, 2, 3, 3, 4, 4, 5]
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

a = Solution()
p = listNode
pHead = a.deleteDuplication(p)      #这样能保证链表头还是listNode指向的结点，但是整个链表结构会发生改变
print("删除重复结点后链表为：")
while(pHead is not None):
    print(pHead.val)
    pHead = pHead.next
    