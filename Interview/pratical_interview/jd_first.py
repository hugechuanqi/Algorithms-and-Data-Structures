## 紧急疏散
# 输入
# 第一行包含一个正整数n，即树的结点数量（1<=n<=100000）。
# 接下来有n-1行，每行有两个正整数x，y，表示在x和y结点之间存在一条边。(1<=x，y<=n)
# 输出
# 输出仅包含一个正整数，表示所需要的最短时间（每个节点移动一步算1s，允许同时移动，也算1s）
## 首先还得构建树 然后还不知道是否为二叉树？

def TreeDepth(self, pRoot):
    # write code here
    depth = 0
    if pRoot==None:
        return depth
    # depth = depth+1
    # if self.TreeDepth(pRoot.left)==None and self.TreeDepth(pRoot.right)==None:
    nleft = self.TreeDepth(pRoot.left) + 1
    nright = self.TreeDepth(pRoot.right) + 1
    depth = max(nleft, nright)
    return depth


