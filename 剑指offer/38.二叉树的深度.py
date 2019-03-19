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
