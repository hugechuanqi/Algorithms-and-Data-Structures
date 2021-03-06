# 运行时间：24ms，占用内存：5692k
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        
        result=[]
        while listNode.next is not None:    #从前往后逐个节点取值
            result.append(listNode.val)
            listNode = listNode.next
        result.append(listNode.val)
        return result[::-1]

## 测试用例
s = {1,2,3}
listNode = ListNode(list(s)[0])
p = listNode
i = 0
for elem in s:
    if i!=0:
        p.next = ListNode(elem)
        p = p.next
    i = i+1

a = Solution()
print(a.printListFromTailToHead(listNode))

