## 题目：重建二叉树
## 类型：二叉树
## 应用：

## 题目描述：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
## 核心：
## 思路：我们首先根据前序遍历的第一个数字创建根结点，接下来在中序遍历中找到根结点的位置，这样就能确定左、右子树结点的数量；然后分别将左右子树递归划分即可。


# -*- coding:utf-8 -*-
## 扩展：构建前序遍历、中序遍历、后序遍历、层序遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """二叉树相关操作"""
    def reConstructBinaryTree(self, pre, tin):
        """ 重建二叉树，递归实现
        """
        if not pre or not tin:  #判断两个树结构不为空
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])

        root.left = self.reConstructBinaryTree(pre[1:val+1], tin[:val])
        root.right = self.reConstructBinaryTree(pre[val+1:], tin[val+1:])
        return root

    def printFromTopToBottom(self, root):
        """ 从上往下打印二叉树
        """
        if not root:
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

## 测试用例
if __name__ == "__main__":
    pre = [1,2,3,4,5,6,7]
    tin = [3,2,4,1,6,5,7]

    a = Solution()
    root = a.reConstructBinaryTree(pre, tin)
    print(a.printFromTopToBottom(root))

## 测试用例：
# 输入：
# pre = [1,2,3,4,5,6,7,8]
# tin = [4,7,2,1,5,3,8,6]
# 输出：
# 返回重建的二叉树
