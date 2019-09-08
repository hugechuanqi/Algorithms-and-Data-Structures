## 题目：二叉树的深度
## 类型：二叉树，DFS

## 题目描述：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

## 思路：递归计算根结点的左右子树的最大深度，则为该二叉树深度。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        depth = 0
        if pRoot==None:
            return depth
        # depth = depth+1
        # if self.TreeDepth(pRoot.left)==None and self.TreeDepth(pRoot.right)==None:
        nleft = self.TreeDepth(pRoot.left) + 1
        nright = self.TreeDepth(pRoot.right) + 1
        depth = max(nleft, nright)
        return depth


## 另一种较简洁的方法
# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         if pRoot==None:
#             return 0
#         return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1
