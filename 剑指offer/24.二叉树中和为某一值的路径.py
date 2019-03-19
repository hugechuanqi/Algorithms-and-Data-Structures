# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root==None:
            return []
        path=[]
        if root.left==None and root.right==None and root.val==expectNumber:
            # path.append([root.val])
            return [[root.val]]
        else:
            leftPath = self.FindPath(root.left, expectNumber-root.val)
            rightPath = self.FindPath(root.right, expectNumber-root.val)
            for item in leftPath+rightPath:
                path.append([root.val]+item)
        return path
