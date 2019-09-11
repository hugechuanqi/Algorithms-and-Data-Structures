## 题目：删除链表中的某个结点
## 类型：链表

## 思路：

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
    def removeNode(self, head, node):
        """ 删除链表中的某个结点
        """
        if head.val == node.val:
            pre = None
            pre.next = head.next
        elif node.next:
            node.val = node.next.val
            node.next = node.next.next      # 不过下一个的下一个是否为空，都给node.next
        else:
            p = head
            while(p):
                if p.next.val == node.val:
                    p.next = None
                    break
        return head

if __name__ == "__main__":
    Arr = [1,2,3,4,5]
    LL = LinkList()
    head = LL.buildList(Arr)
    print(LL.printLinkList(head))

    a = Solution()
    pRemove = head.next
    head = a.removeNode(head, pRemove)
    print(LL.printLinkList(head))
