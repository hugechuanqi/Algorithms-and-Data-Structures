## 题目：二叉树的镜像
## 类型：二叉树，DFS

## 题目描述：操作给定的二叉树，将其变换为源二叉树的镜像。
## 输入：
# 二叉树的镜像定义：源二叉树 
#     8
#    /  \
#   6   10
#  / \  / \
# 5  7 9 11
# 镜像二叉树
#     8
#    /  \
#   10   6
#  / \  / \
# 11 9 7  5

## 思路：首先判断二叉树是否为空，然后判断左右子树是否为空，如果不为空，则交换左右子树，最后进行左右子树的镜像递归。


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return root
        if root.left==None and root.right==None:
            return root
        (root.left, root.right) = (root.right, root.left)

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
            
        return root
