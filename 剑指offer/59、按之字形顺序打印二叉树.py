## 题目：按之字形顺序打印二叉树
## 类型：二叉树，栈
## 应用：

## 题目类型：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

## 核心：每一层的标记很重要，每一层压入栈中的顺序判断很重要，如何判断某个数组为空很重要。
## 思路：由于需要按照之字形打印，因此属于逐层打印，而每两层之间的打印顺序是反着的，因此需要建立两个栈，交替将当前层的结点打印出来，下一层的结点压入栈中，直到当前层的结点全部打印完毕，那么开始打印当前层的下一层。依次循环，直到两个栈都为空。

# -*- coding:utf-8 -*-
class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

class BinaryTree(object):
    """ 二叉树结构类
    """
    def build_tree(self, List):
        """ 构建一棵平衡二叉树，数组必须为排序好地数组，才能使得是平衡二叉树
                前提：输入中序遍历，该列表必须满足一棵满二叉树，才能取中间结点为根结点，然后左右子树递归
        """
        l=0
        r=len(List)-1
        if(l>r):    # 数组为空
            return None
        if(l==r):   # 数组大小为1
            return TreeNode(List[l])
        mid = int((l+r)/2)
        root=TreeNode(List[mid])    #构造成根结点，然后左右子树递归
        root.left=self.build_tree(List[:mid])
        root.right=self.build_tree(List[mid+1:])
        return root

    def PrintFromTopToBottom(self, root):   #利用队列的先入先出，将左右孩子结点顺序弹出
        """ 从上往下打印二叉树——层序遍历
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

class Solution:
    # def printBranch(self, pRoot):
    #     """ 分行从上到下打印二叉树
    #     """
    #     if not pRoot:
    #         return []
    #     queue1 = []
    #     queue2 = []
    #     layer = 1
    #     queue1.append(pRoot)
    #     while(queue1!=None or queue2!=None):
            
    #         if layer%2!=0:
    #             while(queue1)
    #                node = queue1.pop(0)

    def printZhiOrder(self, pRoot):
        """ 之字形顺序打印二叉树
        """
        if not pRoot:
            return []
        stack = [[],[]]
        result = []
        layerResult = []
        
        current = 0
        next_ =1
        stack[current].append(pRoot)
        while(stack[0] or stack[1]):
            node = stack[current].pop()
            layerResult.append(str(node.val))

            if current == 0:    # 偶数行从左到右打印
                if node.left:
                    stack[next_].append(node.left)
                if node.right:
                    stack[next_].append(node.right)    
            else:                        # 奇数行从右到左打印
                if node.right:
                    stack[next_].append(node.right)
                if node.left:
                    stack[next_].append(node.left)
            
            if not stack[current]:      # 如果当前栈为空
                result.append(layerResult)
                # print(" ".join(layerResult))
                layerResult = []
                current = 1-current
                next_ = 1 - next_
        return result

if __name__ == "__main__":
## 输入：
#                         1
#             2                        3
#     4           5             6         7
#  8   9   10   11    12 13 14 15
# 输出：
# 1
# 3 2
# 4 5 6 7
# 15 14 13 12 11 10 9 8

    Arr = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]   # 输入中序遍历

## 输入：
#                   1
#         2                   3
#     4      0         5           6
# 6    0  0  0    0   0    3     0
# 输出：
# 1
# 3 2
# 4 0 5 6
# 0 3 0 0 0 0 0 6

    # 2、通过数组构造平衡二叉树 
    # Arr = [6, 4, 0, 2, 0, 0, 0, 1, 0, 5, 0, 3, 3, 6, 0]       # 输入中序遍历
    BT = BinaryTree()
    pRoot = BT.build_tree(Arr)
    print("二叉树为：", BT.PrintFromTopToBottom(pRoot), "——对应层序遍历")

    a = Solution()
    print("之字形顺序：", a.printZhiOrder(pRoot))
