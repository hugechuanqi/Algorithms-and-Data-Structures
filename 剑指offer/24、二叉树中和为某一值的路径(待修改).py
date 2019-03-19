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
        path = []
        if root == None:
            return
        currentNum = 0
        # result = []
        self.findPath(root, expectNumber, path, currentNum)
        return path

    def findPath(pRoot, expectNumber, path, currentNum):
        current = current + pRoot.val
        path.append(pRoot.val)

        isleaf = pRoot.left==None and pRoot.right==None
        # flag = root.left == None and root.right == None
        if(currentNum == expectNumber and isleaf):
            print("路径包括")
            print(path)
            print("\n")
            # onepath = []
            # for node in path:
            #     onepath.append(node.val)
            # result.append(onepath)

        if(pRoot.left!=None):
            self.findPath(pRoot.left, expectNumber, path, currentNum)
        if(pRoot.left!=None):
            self.findPath(pRoot.right, expectNumber, path, currentNum)
        
        path.pop()  #拿到一个正确的路径后要弹出，回到上一次父结点继续递归
        # return result
            
        
## 如何存储路径？如何设定初始值？