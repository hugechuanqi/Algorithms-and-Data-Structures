# coding: utf-8
# 参考：https://www.cnblogs.com/liutongqing/p/7698429.html

class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def is_empty(self, self):
        return self.root == None
    
    def preOrder(self, BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        
        print(BinaryTreeNode.data)
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def inOrder(self, BinaryTreeNode):
        if BinaryTreeNode == None:
            reurn

        self.inOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.left)
        self.inOrder(BinaryTreeNode.right)

    def postOrder(self, BinaryTreeNode)
        if BinaryTreeNode == None:
            reurn

        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.left)


if __name__ == "__main__":
    Arr = ["D", "E", "F", "B", "C", "A"]
    n1 = BinaryTreeNode(data="D")
    n2 = BinaryTreeNode(data="E")
    n3 = BinaryTreeNode(data="F")
    n4 = BinaryTreeNode(data="B", left=n1, right=n2)
    n5 = BinaryTreeNode(data="C", left=n3, right=None)
    root = BinaryTreeNode(data="A", left=n4, right=n5)

    bt = BinaryTree(root)
    print('先序遍历')
    bt.preOrder(bt.root)
    print('中序遍历')
    bt.inOrder(bt.root)
    print('后序遍历')
    bt.postOrder(bt.root)

