## 题目：对称的二叉树（52ms）
## 类型：二叉树，深度优先搜索，广度优先搜索
## 应用：

## 题目描述：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
## 输入：
#      1
#    /    \
#   2      2
#  / \    / \
# 3  4 4  3
# 输出：
# True

## 核心：主要是取两个结点进行亮亮判断。
## 思路：首先判断二叉树A和复制二叉树B是否同时为空，如果两个二叉树都不为空，就判断根结点值是否相等，然后判断A的左子树是否和B的右子树相同（即镜像对称），同时还满足A的右子树和B的左子树相同，是则对称，否则不对称。

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

    def Mirror(self, root):
        """ 构造二叉树镜像
        """
        if root == None:
            return root
        if root.left==None and root.right==None:
            return root
        (root.left, root.right) = (root.right, root.left)   # 不断交换二叉树的子树

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
            
        return root

class Solution:
    """ 判断一棵二叉树是否为对称的二叉树
    """
    def isSymmetrical(self, pRoot):
        """ 递归实现：比较二叉树的前序遍历序列和对称前序遍历序列是否相同
        """
        return self.IsSym(pRoot, pRoot)
    def IsSym(self, pRoot1, pRoot2):
        if pRoot1==None and pRoot2==None:
            return True
        if pRoot1 == None or pRoot2 == None:    # 继承了前面的判断：即不可能同时为空
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IsSym(pRoot1.left, pRoot2.right) and self.IsSym(pRoot1.right, pRoot2.left) 

    def isSymmetrical2(self, pRoot):
        """ 队列实现：注意添加树的左右子树的顺序即可
        """
        queue = []
        queue.append(pRoot)
        queue.append(pRoot)

        while(len(queue)>=2):     # 循环条件时队列中为空，由于没判断left和right是否为空，因此存在加入队列为空的情况
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            if t1.left and t2.right:
                queue.append(t1.left)
                queue.append(t2.right)
            if t1.right and t2.left:
                queue.append(t1.right)
                queue.append(t2.left)
        return True

if __name__ == "__main__":
## 输入：
#      1
#    /    \
#   2      2
#  / \    / \
# 3  4 4  3
    Arr = [3,2,4,1,4,2,3]
    BT = BinaryTree()
    pRoot = BT.build_tree(Arr)
    print("层序遍历为：", BT.PrintFromTopToBottom(pRoot))      # 层序遍历打印一边二叉树
    pRoot_Mirror = BT.Mirror(pRoot)
    print("二叉树镜像层序遍历为：", BT.PrintFromTopToBottom(pRoot_Mirror))      # 层序遍历打印一边二叉树

    a = Solution()
    print(a.isSymmetrical2(pRoot))
