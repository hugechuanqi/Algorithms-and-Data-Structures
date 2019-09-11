## 题目：链表中环的入口节点
## 类型：链表，快慢指针+双指针，环结构
## 题目应用：快慢指针应用于环结构，双指针应用于保持指针之间的间隔性

## 题目描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
## 核心：1、快慢指针判断是否存在环；2、确定环的长度；3、找到环的入口节点
## 思路：1、首先分别定义两个快慢指针，同时从头节点出发，如果走得快的指针走到了链表的末尾（认为指向NULL），都没有追上第一个指针，则认为链表中不包含环，如果两个指针又指向了同一个节点，则认为存在环。2、当追上时，开始移动慢指针并且开始从0计数，当再次指向该位置时，则计数值为环的长度k。3、确定环的长度之后，重新开始遍历，双指针p、q指向头节点，后移q指针k步，然后同时移动p、q指针，当两个指针再次相遇时，相遇的位置则为链表中环的入口节点。
## 核心2：当快慢指针行走节点数为2x、x相遇时，相当于快指针比慢指针多走了一个环的长度n，则有2x-x=n，得到n=x，即慢指针指向的位置离头指针距离为n
## 问题：如何建立一个链表——完成，在List当中

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class List:
    """ 建立链表
    """
    def buildListLoop(self, Arr):       #此处在第3个位置定义为q，然后让链表尾节点的下一个节点指向q
        """ 建立链表环结构
        """
        head = ListNode(Arr[0])
        p = head
        for i in range(1, len(Arr)):
            if i==2:
                p.next = ListNode(Arr[i])   # 由于next还不是一个列表，因此需要将p.next建立成一个列表
                p = p.next
                q = p
            else:
                p.next = ListNode(Arr[i])
                p = p.next
        p.next = q  # 建立环结构
        # print(q.val, p.val, head.val)
        return head

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

class Solution:
    """ 判断链表中环的入口节点解决方案
    """
    def checkLoop(self, head):
        """ 检查是否存在环
        """
        quick = head
        slow =  head
        while(quick.next):      # 如果有环，那么quick.next一定不为空
            quick = quick.next.next     # 快指针走两步
            slow = slow.next                   # 慢指针走一步
            if quick == slow:
                return True
            if not quick:               # 防止当前结点为空，则quick.next不存在，会报错
                return False
        return False

    def EntryNodeOfLoop(self, head):
        """ 获取链表环的入口节点
        """
        if not head:
            print('null')   # 表示不存在环结构
            return
        if not self.checkLoop(head):
            print('null')   # 表示不存在环结构
            return
        else:
            # print('存在环结构')
            # 1、从头结点开始，找到相交的位置
            quick = head
            slow =  head
            while(quick.next):
                quick = quick.next.next     # 快指针走两步
                slow = slow.next                   # 慢指针走一步
                if quick == slow:
                    break

            # 2、从相交的位置开始，再次移动其中一个指针，当再次与另一个指针相交时，其移动次数环的长度
            slow = slow.next
            count = 1
            while(quick!=slow):
                slow = slow.next
                count += 1

            # 3、建立双指针，指向头结点，让q先移动环长度的步数，然后一起后移，直到两个指针相交，则相交的位置就是环的起点
            p,q = head, head
            while(count>0):
                q = q.next
                count -= 1
            while(p!=q):
                p = p.next
                q = q.next
            return p

    def EntryNodeOfLoop2(self, head):
        """ 获取链表环的入口节点——减少了计算环长度步骤和控制双指针间隔的步骤（2x-x=n）
        """
        if not head:
            print('null')
            return
        if not self.checkLoop(head):
            print('null')
            return
        else:
            # print("存在环结构")
            quick = head
            slow =  head
            while(quick.next):
                quick = quick.next.next     # 快指针走两步
                slow = slow.next                   # 慢指针走一步
                if quick == slow:
                    break

            quick = head
            while(quick!=slow):
                slow = slow.next
                quick = quick.next
            return quick
            

if __name__ == "__main__":
    Arr = [1,2,3,4,5,6]     # 环中的6节点是指向3节点的
    a = List()
    head = a.buildListLoop(Arr)
    # head = a.buildList(Arr)
    # print(head.val, head.next.val, head.next.next.next.next.next.next.val)
    b = Solution()
    p = b.EntryNodeOfLoop(head)
    print(p)

## 测试用例：
# 输入：
# [1,2,3,4,5,6,7,8,9,5]
# 输出：
# 5