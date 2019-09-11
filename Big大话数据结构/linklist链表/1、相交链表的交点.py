## 题目：寻找两个相交链表的交点
## 类型：链表操作

## 题目描述：

## 思路：1、首先寻找两个链表的长度m,n；2、然后后移较长的链表|m-n|步；3、最后一起移动，直到找到相交的交点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def buildList(self, Arr):
        """ 建立链表
        """
        if not Arr:
            return None
        head = ListNode(Arr[0])
        p = head
        for i in range(1, len(Arr)):
            p.next = ListNode(Arr[i])
            p = p.next
        return head

    def printLinkList(self, head):
        """ 打印链表
        """
        if not head:
            return None
        result = []
        p = head
        while(p):
            result.append(p.val)
            p = p.next
        return result

class Solution:
    def getLinkLength(self, head):
        """ 获取链表长度
        """
        length = 0
        p = head
        while(p):
            length +=  1
            p = p.next
        return length
    def intersection(self, head1, head2):
        """ 获取交叉点
        """
        if not head1 or not head2:
            return None
        
        # 1、获取长度
        length1 = self.getLinkLength(head1)
        length2 = self.getLinkLength(head2)

        p,q = head1, head2
        # 1、根据链表长度大小分情况找交叉点
        if length1==length2:
            pIntersection = self.moveTogether(p, q)
        elif length1>length2:
            K = length1 - length2
            for i in range(K):
                p = p.next
            pIntersection = self.moveTogether(p, q)
        elif length1<length2:
            K = length2 - length1
            for i in range(K):
                q = q.next
            pIntersection = self.moveTogether(p,q)
        return pIntersection

    def moveTogether(self, p,q):
        """ 一起移动
        """
        while(p):
            if p.val==q.val:
                return p
            p = p.next
            q = q.next
        return None

if __name__ == "__main__":
    Arr = [1,2,3,4,5]
    Arr2 = [0,2,1,3,9,3,4,5]
    LL = LinkList()
    head1 = LL.buildList(Arr)
    head2 = LL.buildList(Arr2)
    print(LL.printLinkList(head1))
    print(LL.printLinkList(head2))

    a = Solution()
    pIntersection = a.intersection(head1, head2)
    print(LL.printLinkList(pIntersection))

