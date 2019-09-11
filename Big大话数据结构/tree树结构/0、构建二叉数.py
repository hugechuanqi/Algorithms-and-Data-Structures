## 题目：构建二叉数

## 题目描述：尝试用前序遍历、中序遍历、后续遍历的方式构建一棵二叉数

class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

class BinaryTree(object):
    """ 二叉树结构类
    """
    def build_tree(self, List):
        """ 构建一棵中序遍历二叉数
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
    
    def build_tree_level(self, nodeList):
        """ 构建一棵层序遍历二叉数
        """
        if nodeList[0] == None:
            return None
        head = TreeNode(nodeList[0])
        Nodes = [head]
        j = 1
        for node in Nodes:
            if node != None:
                node.left = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
                Nodes.append(node.left)
                j += 1
                if j == len(nodeList):
                    return head
                node.right = (TreeNode(nodeList[j])if nodeList[j] != None else None)
                j += 1
                Nodes.append(node.right)
                if j == len(nodeList):
                    return head

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

if __name__ == "__main__":
# 输入：
#                     9
#          6                      15
#     2         -1        12      25
# -1 -1   -1 -1   -1 -1    20 37

    Arr = [9 ,6 ,15 ,2 ,-1 ,12 ,25 ,-1, -1, -1, -1, -1, -1, 20, 37]
    BT = BinaryTree()
    pRoot_pre = BT.build_tree(Arr)
    print("中序遍历产生的二叉数", BT.PrintFromTopToBottom(pRoot_pre))

    pRoot_level = BT.build_tree_level(Arr)
    print("层序遍历产生的二叉数", BT.PrintFromTopToBottom(pRoot_level))
