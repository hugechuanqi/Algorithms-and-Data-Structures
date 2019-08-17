# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    ## 面向对象添加一个节点值
    # def build(self, Value):
    #     return self.val.add(Value)

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        
        result=[]
        p = listNode
        while(p is not None):
            result.insert(0, p.val)
            p = p.next
        return result

## 测试用例
if __name__ == "__main__":
    s = {1,2,3}
    ## --- 此过程为建立链表的过程
    listNode = ListNode(list(s)[0])
    p = listNode
    i = 0
    for value in s:
        i = i + 1
        if i ==1:
            continue
        else:
            p.next = ListNode(value)
            p = p.next
    ## ---

    a = Solution()
    print(a.printListFromTailToHead(listNode))

