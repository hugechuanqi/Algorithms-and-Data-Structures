## 题目：二叉数中和为某一值的路径
## 类型：二叉树，深度优先搜索
## 应用：按照固定值求所有路径（常用于图算法）

## 题目描述：输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
## 输入：14
#                   1
#         2               3
#     4            5          6
# 7                        8
# 输出：
# 1->2->4->7

## 核心：首先找到遍历方式，然后判断从根结点到每一个叶结点的路径和是否等于某一值。
## 思路：由于路径是从根结点出发到叶子结点，也就是数路径总是以根结点为起始点，因此我们需要用前序遍历才能首先访问到根结点。具体过程如下：当用前序遍历的方式访问到某一结点时，我们把该结点添加到路径中，并累加该结点的值；如果该结点为叶结点，并且路径中结点值的和刚好等于输入的整数，则当前路径符合要求；如果当前结点不是叶结点，则继续访问它的子节点；**当前结点访问结束后，递归函数将自动回到它的父结点。**


# -*- coding:utf-8 -*-
class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

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
    """ 解决二叉树中和为某一值的路径
    """
    def FindPath(self, root, expectNumber):
        """ 二叉数中和为某一值的路径
        """
        if root==None:      # 判断为空和判断找到路径对递归很重要
            return []
        path=[]     # 里面放置多个数组，用于存储每一个路径
        if root.left==None and root.right==None and root.val==expectNumber:
            return [[root.val]]
        else:
            leftPath = self.FindPath(root.left, expectNumber-root.val)
            rightPath = self.FindPath(root.right, expectNumber-root.val)
            for item in leftPath+rightPath:
                # print([root.val], item)
                path.append([root.val]+item)
        return path

    def FindPath2(self, pRoot, expectNumber):
        """ 二叉树中和为某一值的路径（C++思想），但是还是出现了一些问题，pyton还不够熟练
        """
        if not pRoot:
            return []
        result = []
        path = []
        currentSum = 0
        self.Find2(pRoot, expectNumber, path, currentSum, result)
        return result
    def Find2(self, pRoot, expectNumber, path, currentSum, result):
        currentSum += pRoot.val
        path.append(pRoot.val)
        
        isLeaf = pRoot.left==None and pRoot.right==None
        # print(path, currentSum, isLeaf)
        if currentSum==expectNumber and isLeaf:
            result.append(path)
        
        if pRoot.left != None:
            self.Find2(pRoot.left, expectNumber, path, currentSum, result)
        if pRoot.right != None:
            self.Find2(pRoot.right, expectNumber, path, currentSum, result)
        path.pop()

if __name__ == "__main__":
## 输入：13
#                   1
#         2               3
#     4            5          6
# 6                        3

    # 2、通过数组构造平衡二叉树 
    Arr = [6, 4, 0, 2, 0, 0, 0, 1, 0, 5, 0, 3, 3, 6, 0]       # 输入中序遍历
    BT = BinaryTree()
    pRoot = BT.build_tree(Arr)
    print("二叉树为：", BT.PrintFromTopToBottom(pRoot), "——对应层序遍历")

    expectNumber = 13
    a = Solution()
    path = a.FindPath2(pRoot, expectNumber)
    print("二叉树中和为某一值的路径：", path)