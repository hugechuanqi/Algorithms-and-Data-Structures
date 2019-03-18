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
            result.extend(listNode.val)
            listNode = listNode.next
        result.extend(listNode.val)
        return result[::-1]

## 测试用例
s = {1,2,3}
listNode = ListNode(s)
# for i in range(len(s)):
#     listNode.val = s[0]
#     listNode = listNode.next
a = Solution()
print(a.printListFromTailToHead(listNode))

