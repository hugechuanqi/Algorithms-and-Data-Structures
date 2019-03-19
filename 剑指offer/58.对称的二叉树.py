# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.IsSymmetrical(pRoot, pRoot)

    def IsSymmetrical(self, pRoot1, pRoot2):
        if pRoot1==None and pRoot2==None:
            return True
        if pRoot1 == None or pRoot2 == None:    #加入两边结点一个为空，一个不为空，那么将出现
                                                #'NoneType' object has no attribute 'val'
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IsSymmetrical(pRoot1.left, pRoot2.right) and self.IsSymmetrical(pRoot1.right, pRoot2.left) 