# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        pRoot2 = self.Mirror(pRoot)
        return self.IsSymmetrical(pRoot, pRoot2)    #将树与其镜像树做对比

    def IsSymmetrical(self, pRoot1, pRoot2):
        if pRoot1==None and pRoot2==None:
            return True
        if pRoot1==None or pRoot2==None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IsSymmetrical(pRoot1.left, pRoot2.left) and self.IsSymmetrical(pRoot1.right, pRoot2.right)

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

###本题如果用镜像函数做，递归时每个中间结点对应的树都得重新生成镜像函数，而我们只需要生成整体树的镜像，而不是子树镜像###