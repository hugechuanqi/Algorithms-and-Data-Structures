# 结点类
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

# 单链表类
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # 定义一个链表结点
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    # 弹出链表结点，并返回该结点数据域
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    # 在链表最后插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 弹出链表最后元素，并返回数据域
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  #直到p.next是最后结点
                p = p.next
        e = p.next.elem
        p.next = None
        return e

    # 找到满足给定条件的表元素
    def find(elf, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    # 查看当前链表情况
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end=' ')
            if p.next is not None:
                print(', ', end= '')
                

## 测试用例
listnode = LNode(1)
p = listnode
for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = listnode
while p is not None:
    print(p.elem)
    p = p.next
