# 如果一棵树的左、右子树深度相差不超过1，则这棵树是平衡的；
# 得判断每一棵子树的深度差都不超过1，这样才能是平衡二叉树。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        
        nleft = self.treeDepth(pRoot.left)
        nright = self.treeDepth(pRoot.right)
        if abs(nleft-nright)>1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def treeDepth(self,pRoot):
        if not pRoot:
            return 0
        # if pRoot.left: 
        #     nleft = self.treeDepth(pRoot.left)+1
        # if pRoot.right:
        #     nright = self.treeDepth(pRoot.right)+1
        nleft = self.treeDepth(pRoot.left)+1
        nright = self.treeDepth(pRoot.right)+1
        
        return max(nleft,nright)
