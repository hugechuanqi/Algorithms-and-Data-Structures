## 题目：寻祖问总
## 类型：二叉查找数，根据层序遍历建立二叉数，然后输出中序遍历结果

## 题目描述：姓氏是人的符号标志，是家族血脉的传承；族谱是家族血脉传承的文字记载。同姓的两个中国人，根据族谱或许能够查出上面几代内是同一个祖先。查一下族谱，也许当代某位同姓名人就是你的远房亲戚，惊喜不惊喜，意外不意外！！！‘
# 二元查找树（1.若左子树不空，左子树值都小于父节点；2.如右子树不空，右子树值都大于父节点；3.左、右子树都是二元查找树；4. 没有键值相等的节点）上任意两个节点的值，请找出它们最近的公共祖先。

# 输入三行行，第一行为树层级，第二行为数节点（其中-1表示为空节点），第三行为需要查找祖先的两个数。

# 在例图中（虚线框没有真实节点，为了输入方便对应位置输-1）查找12和20的最近公共祖先输入为：

# 4

# 9 6 15 2 -1 12 25 -1 -1 -1 -1 -1 -1 20 37

# 12 20

# 输出：
# 输出给出两个数在树上的最近公共祖先数值，如果没有公共祖先，输出-1；如果其中一个节点是另一个节点的祖先，输出这个祖先点（如例图中找15、20最近公共祖先，输出15）；如果输入无效，输出-1。


## 思路：层序遍历转中序遍历的过程

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    def build_tree(self, nodeList):
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

    def PrintFromTopToBottom(self, root): 
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

class Solution:
    def inOrder(self, pRoot):
        if not pRoot:
            return []
        result = []
        stack = []

        p = pRoot
        while(p or stack):
            while(p): 
                stack.append(p)
                p = p.left
            if stack: 
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result

if __name__ == "__main__":
    # Arr = [9 ,6 ,15 ,2 ,-1 ,12 ,25 ,-1, -1, -1, -1, -1, -1, 20, 37]
    # r1, r2 = 12, 20
    length = int(input())
    Arr = list(map(int, input().split()))
    r1, r2 = list(map(int, input().split()))

    BT =BinaryTree()
    pRoot = BT.build_tree(Arr)
    # print(BT.PrintFromTopToBottom(pRoot))

    a = Solution()
    result = a.inOrder(pRoot)
    # print(result)
    first = result.index(r1)
    second = result.index(r2)
    if r1==Arr[0] or r2==Arr[0] or first==second:
        print("-1")
    elif second>first:
        res = result[first:second]
        res.remove(-1)
        if len(res)==1:
            print(res[0])
        elif len(res)==2:
            print(res[1])
        else:
            print(res[int(len(res)/2)])
    elif second<first:
        res = result[second:first]
        res.remove(-1)
        if len(res)==1:
            print(res[0])
        elif len(res)==2:
            print(res[1])
        else:
            print(res[int(len(res)/2)])



## 测试用例：
# 输入：
# 4
# 9 6 15 2 -1 12 25 -1 -1 -1 -1 -1 -1 20 37
# 12 20
# 输出：
# 15
