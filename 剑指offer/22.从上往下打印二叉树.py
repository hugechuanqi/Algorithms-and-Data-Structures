# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
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

if __name__ == "__main__":
    """如何建立一颗二叉树：前序遍历+中序遍历+后序遍历+层序遍历"""
    s = {10,6,14,4,8,12,16}

# class Solution:
#     # 返回从上到下每个节点值列表，例：[1,2,3]
#     def PrintFromTopToBottom(self, root):
#         # write code here
#         result = []
#         result = self.AddRootPoint(root,result)
#         return result

#     def AddRootPoint(self. root, result):
#         result.append(root.val)
#         if root.left:
#             self.AddRootPoint(root.left)
#         if root.right:
#             self.AddRootPoint(root.right)
#         return result