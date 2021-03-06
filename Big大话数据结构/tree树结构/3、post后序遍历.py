# coding: utf-8
# 参考：https://www.cnblogs.com/liutongqing/p/7698429.html
# 参考：https://www.cnblogs.com/llhthinker/p/4747962.html

## 题目描述：二叉树的构建和后序遍历的递归/非递归实现。
## 测试用例：
# 输入：
#             A
#     B           C
# D     E     F     #
# 输出：
# DEBF#CA

## 方法二：使用一个一个栈实现，具体过程如下：
# 1、申请一个栈，记为stack，将头结点压入栈stack中，同时设置两个变量h和c，在整个流程中，h代表最近一次弹出并打印的结点，c代表当前stack的栈顶结点，初始时令h为头结点，c为null。
# 2、每次令c等于当前stack的栈顶结点，但是不从stack中弹出结点，此时分一下三种情况：
# （1）如果c的左孩子结点为不为空，并且h不等于c的左孩子，也不等于c的右孩子，则把c的左孩子压入stack中。
# （2）如果情况1不成立，并且c的右孩子不为空，并且h不等于c的右孩子，则把c的右孩子压入stack中。
# （3）如果情况1和情况2都不成立，那么从stack中弹出c并打印，然后令h等于c。

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
        while len(queue)>0: 
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    
    def postOrder(self, pRoot):
        """ 递归实现二叉树的后序遍历
        """
        if pRoot == None:
            return

        self.postOrder(pRoot.left)
        self.postOrder(pRoot.right)
        print(pRoot.val)

    def postOrder2(self, pRoot):
        """ 非递归实现二叉树的后序遍历——思想：DFS深度优先搜索，后序遍历和层序遍历很相似，只不过每次将输出值放在列表前列
        """
        if not pRoot:
            return []
        stack = []
        result = []

        stack.append(pRoot)
        while len(stack)>0:  
            node = stack.pop()
            result.insert(0, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
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

    result = BT.postOrder3(pRoot)
    print("后序遍历：", result)
