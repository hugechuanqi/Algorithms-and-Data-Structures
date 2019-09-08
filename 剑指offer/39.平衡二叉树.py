## 题目：平衡二叉树
## 类型：二叉树
## 应用：

## 题目描述：输入一棵二叉树，判断该二叉树是否是平衡二叉树。如果某二叉树中任意结点的左、右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
## 平衡二叉树定义： 如果一棵树的左、右子树深度相差不超过1，则这棵树是平衡的；得判断每一棵子树的深度差都不超过1，这样才能是平衡二叉树。
## 二叉排序树（二叉查找树）：左子树上所有结点的值均小于它的根结构的值，右子树上所有的值大于它的根结构的值。

## 核心：1、首先判断根结点是否为空；2、然后判断整个树两侧的深度差；3、最后递归判断左右子树两侧的深度差。
## 思路：判断每一层结点的的子树深度，但凡不满足左右子树深度差小于等于1，则不是平衡二叉树，相反则为平衡二叉树。                                                                                                                                         
## 注意：Solution类中解决方法是解决本问题的方法，Solution2是另外一种方法，其他类只是一种辅助作用。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    ## 建立一棵平衡二叉树：选定一个中间值，左子树的值比根结点值小，右子树的值比根结点大。
    def build_tree(self, List):
        """ 构建一棵平衡二叉树，数组必须为中序遍历类型，如果数组排好序，那么得到平衡二叉树
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
        """ 从上往下打印二叉树
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
    """ 从上往下遍历时，由于每次计算结点深度时，其下面的结点都会被遍历到，导致多次访问，影响性能
    """
    def IsBalanced_Solution(self, pRoot):
        """ 判断是否为平衡树
        """
        if not pRoot:
            return True
        
        nleft = self.treeDepth(pRoot.left)
        nright = self.treeDepth(pRoot.right)
        if abs(nleft-nright)>1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)   # 不仅要判断整个树两侧的深度差（平衡差）是否小于等于1，而且还需要判断左子树和右子树两侧的深度差

    def treeDepth(self,pRoot):
        """ 计算二叉树的深度
        """
        if not pRoot:
            return 0

        nleft = self.treeDepth(pRoot.left)+1
        nright = self.treeDepth(pRoot.right)+1
        return max(nleft,nright)

class Solution2:
    """ 从下往上遍历，如果子树是平衡二叉树，则返回子树的高度；如果子树不是平衡二叉树，则直接停止遍历，这样只需要对每个结点访问一次
    """
    def IsBalanced_Solution(self, pRoot):
        return self.getDepth(pRoot) != -1

    def getDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left)
        if left==-1:
            return -1
        right = self.getDepth(pRoot.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        else:
            return 1 + max(left, right)

if __name__ == "__main__":
    Arr = [55555,333,1,22,4444,666666]
    # 1、构建平衡二叉树
    a = BinaryTree()
    # Arr = sorted(Arr)  # 将数组进行排序，是为了能够得到平衡二叉排序树，否则得到的只是平衡二叉树，并非二叉排序树
    pRoot = a.build_tree(Arr)
    print("二叉树为：", a.PrintFromTopToBottom(pRoot))

    # 2、判断是否为平衡二叉树
    b = Solution2()
    if b.IsBalanced_Solution(pRoot):
        print(True, "是平衡二叉树")
    else:
        print(False, "不是平衡二叉树")
