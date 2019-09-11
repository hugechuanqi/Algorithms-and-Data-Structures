## 找到链表中倒数第k个结点
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
    def checkLoop(self, head):
        """ 快慢指针检测链表是否有环
        """
        quick = head
        slow = head
        while(quick.next):
            quick = quick.next.next
            slow = slow.next
            if quick==slow:
                return True
            if not quick:
                return False
        return False
    
    def EnterNodeOfLoop(self, head):
        """ 获取链表中环的入口结点
        """
        if not head or not head.next:
            return None
        if not self.checkLoop(head):
            return None
        else:
            # 1、快慢指针
            # 2、环的长度
            # 3、环的起点位置

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