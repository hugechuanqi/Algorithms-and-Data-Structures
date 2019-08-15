# coding: utf-8
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        # print(pre[0])

        root.left = self.reConstructBinaryTree(pre[1:val+1], tin[0:val])
        root.right = self.reConstructBinaryTree(pre[val+1:], tin[val+1:])
        return root

    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        queue = []
        result = []

        queue.append(root)
        while(len(queue)>0):
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

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
                print(leftPath, rightPath, [root.val]+item)
                path.append([root.val]+item)
        return path

if __name__ == "__main__":
    pre = [1,2,3,4,5,6,7,8]
    tin = [3,2,4,1,6,5,7,8]
    a = Solution()
    root = a.reConstructBinaryTree(pre, tin)
    result = a.PrintFromTopToBottom(root)
    print(result)
    path = a.FindPath(root, 7)
    print(path)