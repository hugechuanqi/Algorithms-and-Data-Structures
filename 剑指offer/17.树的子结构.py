# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    """ 二叉树结构类
    """
    def build_tree(self, List):
        """ 构建一棵平衡二叉树，数组必须为排序好地数组，才能使得是平衡二叉树
                前提：输入中序遍历，该列表必须满足一棵满二叉树，才能取中间结点为根结点，然后左右子树递归
        """
        l=0
        r=len(List)-1
        if(l>r):    # 数组为空
            return None
        if(l==r):   # 数组大小为1
            return TreeNode(List[l])
        mid = int((l+r)/2)
        root=TreeNode(List[mid])    #构造成根结点，然后左右子树递归
        root.left=self.build_tree(List[:mid])
        root.right=self.build_tree(List[mid+1:])
        return root

    def PrintFromTopToBottom(self, root):   #利用队列的先入先出，将左右孩子结点顺序弹出
        """ 从上往下打印二叉树——层序遍历
        """
        if not root:
            return []
        queue = []
        result = []

        queue.append(root)
        while len(queue)>0:     #while(len(queue)>0):不知道为什么就错了
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):   
        """ 递归实现：判断二叉树B是否为二叉树A的子结构，首先找到相同根结点
        """
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.same(pRoot1, pRoot2)
            if not result:      #如果根结点不相同，则从树的左右子结点继续寻找
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    def same(self, pRoot1, pRoot2):
        """ 如果根结点相同，则分别判断左右子结点是否相同，直到二叉树B的子节点为空
        """
        if pRoot2 == None:
            return True
        if pRoot1 == None or pRoot1.val != pRoot2.val:
            return False
        return self.same(pRoot1.left, pRoot2.left) and self.same(pRoot1.right, pRoot2.right)

    def HasSubtree2(self, pRoot1, pRoot2):
        """ 非递归实现：判断二叉树B是否为二叉树A的子结构，首先找到相同根结点
        """
        if not pRoot1 or not pRoot2:
            return False
        queue = []

        queue.append(pRoot1)
        while(queue):
            node = queue.pop(0)
            if node.val==pRoot2.val and self.checkSame(node, pRoot2):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    def checkSame(self, pRoot1, pRoot2):
        """ 如果根结点相同，则分别判断左右子节点是否相同，直到二叉树B的子节点为空
        """
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val!=pRoot2.val:
            return False
        return self.checkSame(pRoot1.left, pRoot2.left) and self.checkSame(pRoot1.right, pRoot2.right)


if __name__ == "__main__":
    ## 测试用例
# 输入树结构为：
#                   8
#         8                   7
#     9       2       '#'       '#'
# '#' '#' 4 7 '#' '#' '#' '#'

    A = ['#', 9, '#', 8, 4, 2, 7, 8, '#', '#', '#', 7, '#', '#', '#']   # 中序遍历
    B = [9, 8, 2]
    # B1 = [9,8,3]
    BT = BinaryTree()
    pRootA = BT.build_tree(A)
    pRootB = BT.build_tree(B)
    print("二叉树A结构（层序遍历）为：", BT.PrintFromTopToBottom(pRootA))
    print("二叉树B结构（层序遍历）为：", BT.PrintFromTopToBottom(pRootB))

    a = Solution()
    print(a.HasSubtree2(pRootA, pRootB))

