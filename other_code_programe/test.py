from collections import deque
class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    # #setter and getter
    # def get_val(self):
    #     return self.val
    # def set_val(self,val):
    #     self.val=val
    # def get_left(self):
    #     return self.left
    # def set_left(self,left):
    #     self.left=left
    # def get_right(self):
    #     return self.right
    # def set_right(self,right):
    #     self.right=right

class Tree:
    def __init__(self, List):
        List = sorted(List)
        self.root=self.build_tree(List)

    ## 建立一棵平衡二叉树：选定一个中间值，左子树的值比根结点值小，右子树的值比根结点大。
    def build_tree(self, List):
        l=0
        r=len(List)-1
        if(l>r):
            return None
        if(l==r):
            return TreeNode(List[l])
        mid = int((l+r)/2)
        root=TreeNode(List[mid])    #构造成根结点，然后左右子树递归
        root.left=self.build_tree(List[:mid])
        root.right=self.build_tree(List[mid+1:])
        return root

    ## 前序遍历：根结点->左结点->右结点
    def preorder(self, root):
        if(root is None):
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    ## 中序遍历：左结点->根结点->右结点
    def inorder(self, root):
        if(root is None):
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    ## 后序遍历：左结点->右结点->根结点
    def postorder(self, root):
        if(root is None):
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    ## 层序遍历：广度优先搜索，同一层次先输出，不同层次后输出
    def levelorder(self, root):
        if root is None:
            return
        queue = deque([root])
        while len(queue)>0:
            size = len(queue)
            for i in range(size):
                node =queue.popleft()
                print(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

list1 = [55555,333,1,22,4444,666666]
#list1=[1,-1,3,4,5]
tree = Tree(list1)
print("前序遍历：")
tree.preorder(tree.root)
print("中序遍历：")
tree.inorder(tree.root)
print("后序遍历：")
tree.postorder(tree.root)
print("层序遍历：")
tree.levelorder(tree.root)
