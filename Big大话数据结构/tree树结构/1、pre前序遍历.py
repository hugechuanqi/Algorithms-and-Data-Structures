# coding: utf-8
# 参考：https://www.cnblogs.com/liutongqing/p/7698429.html
# 参考：https://www.cnblogs.com/llhthinker/p/4747962.html

## 题目描述：二叉树的构建和前序遍历的递归/非递归实现。
## 测试用例：
# 输入：
#             A
#     B           C
# D     E     F     #
# 输出：
# ABDECF#


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
        """
        l=0
        r=len(List)-1
        if(l>r):    # 数组为空
            return None
        if(l==r):   # 数组大小为1
            return TreeNode(List[l])
        if (l+r)%2==0:
            mid = int((l+r)/2)
        else:
            mid = int((l+r)/2)+1
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
    
    def preOrder(self, pRoot):
        """ 递归实现二叉树的先序遍历
        """
        if pRoot == None:
            return

        print(pRoot.val)
        self.preOrder(pRoot.left)
        self.preOrder(pRoot.right)

    def preOrder2(self, pRoot):
        """ 非递归实现二叉树的先序遍历——思想：DFS，但是每次搜索之前都会弹出根结点，这样无法实现不以根结点遍历的结果
        """
        if not pRoot:
            return []
        result = []

        stack = []
        stack.append(pRoot)     # 这种方法只适用于从根结点开始的遍历
        while(len(stack)>0):
            node = stack.pop()
            result.append(node.val)  
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

if __name__ == "__main__":
    # 1、直接拼接二叉树
    # n1 = TreeNode(data="D")
    # n2 = TreeNode(data="E")
    # n3 = TreeNode(data="F")
    # n4 = TreeNode(data="B", left=n1, right=n2)
    # n5 = TreeNode(data="C", left=n3, right=None)
    # root = TreeNode(data="A", left=n4, right=n5)
    #             A
    #     B           C
    # D     E     F     #

    # 2、通过数组构造平衡二叉树 
    Arr = ['D', 'B', 'E', 'A', 'F', 'C', '#']
    BT = BinaryTree()
    pRoot = BT.build_tree(Arr)
    print("二叉树为：", BT.PrintFromTopToBottom(pRoot), "——对应层序遍历")

    result = BT.preOrder(pRoot)
    print("先序遍历：", result)
