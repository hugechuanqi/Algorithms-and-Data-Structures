class Tree:
    def __init__(self, val = '#', left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
 
    #前序构建二叉树
    def FrontBuildTree(self):
        temp = input('Please Input: ')
        node = Tree(temp)
        if(temp != '#'):
            node.left = self.FrontBuildTree()
            node.right = self.FrontBuildTree()
        return node#因为没有引用也没有指针，所以就把新的节点给返回回去
    
    #前序遍历二叉树
    def VisitNode(self):
        print(self.val)
        if(self.val != '#'):
            self.left.VisitNode()
            self.right.VisitNode()
 
if __name__ == '__main__':
    root = Tree()
    root = root.FrontBuildTree()
    root.VisitNode()
    