# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):   #判断树A是否包含树B，其中pRoot1为树A的根结点，pRoot2为树B的根结点
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.same(pRoot1, pRoot2)
            if not result:      #如果False，则从树的左子结点继续寻找
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def same(self, pRoot1, pRoot2):
        # 前面三个判断是为了防止出现错误,并判断子结点是否也满足条件
        if pRoot2 == None:
            return True
        if pRoot1 == None or pRoot1.val != pRoot2.val:
            return False
        return self.same(pRoot1.left, pRoot2.left) and self.same(pRoot1.right1, pRoot2.right)

## 测试用例
A = [8,8,7,9,2,'#','#','#','#',4,7]
B = [8,9,2]
treeA = TreeNode(A)
treeB = TreeNode(B)
# for i in A:
#     treeA.val = i
#     treeA.left = treeA
#     treeA.right = treeA
# for j in B:
#     treeB.val = j
#     treeB.left = treeB
#     treeB.right = treeB
a = Solution()
print(a.HasSubtree(treeA, treeB))

