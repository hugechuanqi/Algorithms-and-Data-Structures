## 题目：复杂链表的复制
## 类型：链表

## 题目描述：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# 核心：1、复制原始链表并添加在原始链表的后面；2、判断原始链表中哪些存在任意指向节点，映射过来；3、将复制之后的链表的偶数位置取出来，则为复制链表，奇数位置为原始链表
# 思路：1、复制原始链表并添加在原始链表的后面；2、判断原始链表中哪些存在任意指向节点，映射过来；3、将复制之后的链表的偶数位置取出来，则为复制链表，奇数位置为原始链表

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    """ 复制复杂链表
    """
    def Clone(self, pHead):
        """ 复制原始链表，(p1,p2,p3)->(p1,p11,p2,p22,p3,p33)
        """
        p = pHead
        while(p):
            pClone = RandomListNode(p.label)
            pClone.next = p.next
            pClone.random = None

            p.next = pClone     # 将p节点下一节点指向复制节点，不过得提前将p节点的下一节点保存下来给复制节点的下一节点
            p = pClone.next     # 然后让p节点变为复制节点得下一节点，即之前p节点得下一节点

        pHead = self.ConnectRandomNodes(pHead)
        pHead = self.ReconnectNodes(pHead)
        return pHead

    def ConnectRandomNodes(self, pHead):
        """ 连接含random的节点，如果原始链表中的N的random指向S，则对应的复制节点N'对应S'
        """
        p = pHead
        while(p):
            pClone = p.next
            if  p.random != None:
                pClone.random = p.random.next

            p = pClone.next
        return pHead

    def ReconnectNodes(self, pHead):
        """ 将链表拆分为两个链表，奇数位置上的节点组成原始链表，偶数位置上的节点组成复制出来的链表
        """
        p = pHead
        pCloneHead = None
        pCloneNode = None

        if p is not None:
            pCloneHead = pCloneNode = p.next    # 复制节点得第一个节点
            p.next = pCloneNode.next
            p = p.next
        
        while(p is not None):       # 逐次移动，p在奇数位置移动，pCloneNode在偶数位置移动
            pCloneNode.next = p.next    # 建立复制节点与复制节点的下一节点得对应
            pCloneNode = pCloneNode.next    # 将复制节点后移一位（相对于复制节点）

            p.next = pCloneNode.next    # 开始转移p节点到原始节点中的下一个节点
            p = p.next
            
        return pCloneHead

if __name__ == "__main__":
    Arr = {1,2,3,4,5,3,5,'#',2,'#'}
    print("因为建立复杂链表的过程也比较麻烦，有时间再做吧")


## 测试用例：
# 输入：
# {1,2,3,4,5,3,5,#,2,#}
# 输出：
# {1,2,3,4,5,3,5,#,2,#}
