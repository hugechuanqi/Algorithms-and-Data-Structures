# # -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def Convert(self, pRootOfTree):
#         # write code here
#         LastNodeInList = ListNode([])
#         LastNodeInList = self.ConvertTreeToList(pRootOfTree, LastNodeInList)
#         return LastNodeInList

#     def ConvertTreeToList(self, pRootOfTree, LastNodeInList):
        
#         if not pRootOfTree:
#             return
#         if not pRootOfTree.left:
#             self.Convert(pRootOfTree.left)
#         LastNodeInList.next = pRootOfTree.left
#         LastNodeInList.next = pRootOfTree

#         if not pRootOfTree.right:
#             self.Convert(pRootOfTree.right)

#         return LastNodeInList

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return

        self.attr = []
        self.midorder(pRootOfTree)
        for i,v in enumerate(self.attr[:-1]):
            v.right = self.attr[i+1]    #向右延伸
            self.attr[i+1].left = v     #向左延伸
        return self.attr[0]

    def midorder(self, root):
        if not root:
            return
        self.midorder(root.left)
        self.attr.append(root)
        self.midorder(root.right)

