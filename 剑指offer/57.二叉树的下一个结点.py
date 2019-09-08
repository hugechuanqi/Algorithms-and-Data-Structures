## 题目：二叉树的下一个结点
## 类型：二叉树，中序遍历
## 应用：

## 题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。（一般是不存在指向父结点的指针）

## 核心：四种可能性：（1）有右子树；（2）无右子树，是父结点的左结点；（3）无右子树，是负结点的有结点；（4）根结点
## 思路：（1）如果一个结点有右子树，那么它的下一个结点就是它的右子树中的最左子节点。从右子节点出发，一直沿着指向左子节点的指针，我们就能找到它的下一个结点。（2）如果一个结点没有右子树，并且该结点是其父结点的左子节点时，那么它的下一个结点就是其父结点。（3）如果一个结点没有右子树，并且该结点还是其父结点的右子节点时，我们沿着指向父结点的指针一直向上遍历，直到找到一个是它父结点地左子节点的结点。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None    # 指向父结点，醉了？？？

class BinaryTree:
    def build_tree(self, List):
        """ 构建一棵二叉树，数组必须为中序遍历类型，如果数组排好序，那么得到平衡二叉树
        """
        l = 0
        r = len(List)-1
        if l>r:
            return None
        if l==r:
            return TreeNode(List[0])

        mid = int((l+r)/2)
        root = TreeNode(List[mid])
        root.left = self.build_tree(List[:mid])
        root.right = self.build_tree(List[mid+1:])
        return root

    def PrintFromTopToBottom(self, root):
        """ 层序遍历二叉树：从上到下打印二叉树
        """
        if not root:
            return []
        queue = []
        result = []

        queue.append(root)
        while(queue):
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

class Solution:
    def GetNextNode(self, pNode):
        """ 找到二叉树中序遍历的下一个结点（尽量不要遍历所有的结点）
        """
        if pNode is None:
            return None
        if pNode.right:     # 如果存在右子树
            p = pNode.right
            while(p and p.left):
                p = p.left
            return p
        if pNode.next:      # 如果不存在右子树，而存在父结点时
            if pNode==pNode.next.left:
                return pNode.next
            elif pNode == pNode.next.right:
                p = pNode.next
                while(p and p.next):    # 当前结点就没有父结点或者一直找到没有父结点
                    if p==p.next.left:  # 找到一个时其父结点的左子节点
                        return p.next
                    else:
                        p = p.next
                return None
        else:
            return None

    def GetNextNode2(self, pNode):
        """ 找到二叉树的下一个结点（对二叉树结点应用的自信版）
        """
        return None

if __name__ == "__main__":
    ## 可以无视此测试区域，因为此题还涉及指向负结点的指针，比较麻烦
    Arr = [55555,333,1,22,4444,666666]      # 中序遍历对应数组
    BT = BinaryTree()
    pRoot = BT.build_tree(Arr)
    print("二叉树层序遍历为：", BT.PrintFromTopToBottom(pRoot))

    a = Solution()
    pNode = pRoot.left
    print(pNode.val, a.GetNextNode(pNode))
