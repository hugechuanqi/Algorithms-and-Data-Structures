# coding: utf-8
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, pRoot, expectNumber):
        if not pRoot:
            return []
        path = []
        currentSum = 0
        return self.Find2(self, pRoot, expectNumber, path, currentSum)
    def Find2(self, pRoot, expectNumber, path, currentSum):
        currentSum += pRoot.val
        path.append(pRoot.val)
        isleaf = (pRoot==None and pRoot==None)

        if isleaf and currentSum==expectNumber:
            print(path)

        if pRoot.left:
            self.FInd2(pRoot.left, expectNumber, path, currentSum)
        if pRoot.right:
            self.Find2(pRoot.right, expectNumber, path, currentSum)
        path.pop()  # 把不符合的当前项弹出

if __name__ == "__main__":
    