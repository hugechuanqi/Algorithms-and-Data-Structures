## 题目：删除链表中重复的结点
## 类型：链表
## 实际应用：扩展单链表的逆转函数

## 题目描述1：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间内删除该结点。
## 题目描述2：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

## 思路1：针对题目1，由于不知道该链表的前一个结点，也就没办法建立删除结点的前一个结点和后一个结点的关系，因此需要遍历链表。方法二：用删除结点的下一节点的内容覆盖该删除结点内容，然后建立该删除结点与下一节点的next的对应，最后删除下一节点并指向空即可，时间复杂度O(1)。前提：要删除的结点确实在链表中。

## 核心2：1、需要判断头结点是否为重复结点，因此需要建立前一结点，其下一节点指向该结点位置；2、然后不断后移判断，若重复需要取出该值，因为很可能有多个重复值；3、注意前一结点pPre的改变（如果重复是不改变的，不重复才后移）
## 思路2：针对题目2，因为不知道头结点是否为重复结点，因此需要新建一个前结点pPre，其下一节点指向头结点；然后建立两个指针，不断后移判断是否重复，如果不重复，则后移一位，并且pPre也后移一位，如果重复，则取出重复值，后移指针判断是否和该值一样，如果一样则继续后移，直到不一样，则pPre的下一节点指向该位置，相当于对之后的链表重复同样的删除重复结点操作。

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
    
    def printListFromHeadToTail(self, listNode):
        """ 从头到尾打印链表
        """
        if not listNode:
            return []
            
        result=[]
        while listNode.next is not None:    #从前往后逐个节点取值
            result.append(listNode.val)
            listNode = listNode.next
        result.append(listNode.val)
        return result

class Solution:
    def deleteListNode(self, pHead, pToBeDeleted):
        """ O(1)时间内删除链表节点，直接用待删除结点的下一个结点的内容覆盖该结点
        """
        if not pHead or not pToBeDeleted:   # 但凡有一个结点为空，则存在问题
            return 

        # 1、开始用下一节点内容覆盖当前结点
        if pToBeDeleted.next is not None:       # 若下一结点不为空
            pToBeDeleted.val = pToBeDeleted.next.val
            p = pToBeDeleted.next
            pToBeDeleted.next = p.next
            del p
            # p = None
        # 2、删除结点为头结点，且下一节点为空（即只含有一个结点）
        elif pHead==pToBeDeleted: 
            del pToBeDeleted
            # pToBeDeleted = None
            pHead = None
        # 3、下一节点为空，且删除结点不为头结点，则还是需要找到前一结点，指向空
        else:
            p = pHead
            while(pHead.next!=pToBeDeleted):
                p = p.next
            p.next = None
            del  pToBeDeleted
            # pToBeDeleted = None
        return pHead

    def deleteDuplication(self, pHead):
        """ 删除链表中重复节点（凡是重复，全部删除）
        """
        if not pHead:
            return None

        pPre = ListNode(None)       # 由于头结点也有可能重复，因此我们需要建立一个指向头结点的指针
        pPre.next = pHead
        head = pPre     # 建立一个输出链表的头结点

        pNode = pHead   # 从头结点开始遍历
        while(pNode is not None):
            ## 1、建立一个pNode和pNext是否重复的flag
            pNext = pNode.next
            duplicated = False
            if pNext is not None and pNode.val == pNext.val:
                duplicated = True

            # 2、删除后续的多个重复结点
            if not duplicated: 
                pPre = pNode    # 相当于不重复时后移
                pNode = pNext
            else: 
                # 删除方式
                value = pNode.val
                while(pNode is not None and pNode.val == value):
                    pNode = pNode.next
                pPre.next = pNode   # 重复时不后移，只是将pPre的下一个指针变一个转向
        return head.next

    def deleteDuplication2(self, pHead):
        if (pHead==None or pHead.next==None):
            return pHead
        Head =  ListNode(0)
        Head.next = pHead
        pre  = Head
        last = Head.next
        while (last!=None):
            if(last.next!=None and last.val == last.next.val):
                while (last.next!=None and last.val == last.next.val):
                    last = last.next
                pre.next = last.next    # 假设存在重复状态，则指针pre指向不变，而指向的下一节点发生改变
                last = last.next
            else:
                pre = pre.next
                last = last.next
        return Head.next


if __name__ == "__main__":
    # Arr = [1, 1, 2, 2, 3, 4, 4, 5,6,7,8]      # 链表
    Arr = [1,1,1,1,1,1,1]
    a = LinkList()
    pHead = a.buildList(Arr)
    print("删除前链表为：", a.printListFromHeadToTail(pHead))

    b = Solution()
    p = pHead
    pHead = b.deleteDuplication(p)      #这样能保证链表头还是listNode指向的结点，但是整个链表结构会发生改变
    print("删除重复结点后链表为：", a.printListFromHeadToTail(pHead))
    

## 测试用例：
# 输入：
# [1, 1, 2, 3, 3, 4, 4, 5,6,7,8]
# 输出：
# [2,5,6,7,8]
