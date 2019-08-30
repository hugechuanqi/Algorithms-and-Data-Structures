## 题目：相同的树
## 类型：二叉树，深度优先搜索
## 应用：

## 题目描述：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
## 输入：
#                   1
#         2               3
#     4            5          6
# 7                        8
# 输入：
#     1                        1
# 2       3               2       3
# 输出：
# True

## 核心：二叉树地递归判断
## 思路：首先判断两个树是否为空，同时空为真，不同时空为假，然后开始判断根结点，并且递归访问根结点的左子树和右子树。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
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

class Solution:
    """ 判断两个树是否为相同结构
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True        
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    pre = [1,2,3,4,5,6,7]    # 前序遍历：根结点->左结点->右结点
    tin =  [3,2,4,1,6,5,7]    # 中序遍历：左结点->根结点->右结点
    a = BinaryTree()
    p = a.reConstructBinaryTree(pre, tin)
    q = a.reConstructBinaryTree(pre, tin)

    b = Solution()
    print(b.isSameTree(p, q))

## 测试用例：
# 输入：
# [1,2,3]
# [1,2,3]
# 输出：
# true
