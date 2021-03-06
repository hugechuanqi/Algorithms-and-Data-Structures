# #题目描述：
# 在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。

# 一些节点 initial 最初被蠕虫感染。只要两个节点直接连接，且其中至少一个节点受到蠕虫的感染，那么两个节点都将被蠕虫感染。蠕虫的传播将继续，直到没有更多的节点可以被这种方式感染。

# 假设 M(initial) 是在蠕虫停止传播之后，整个网络中感染蠕虫的最终节点数。

# 我们可以从初始列表中删除一个节点。如果移除这一节点将最小化 M(initial)， 则返回该节点。如果有多个节点满足条件，就返回索引最小的节点。

# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后可能仍然因蠕虫传播而受到感染。


# 输入：

# 第一行：节点网络的行数

# 中间行：节点网络graph

# 最后一行：受感染节点的列表initial


# 输出：输出能够使M最小化的节点的索引。


# 测试用例：
# 输入：
# 3
# 1 1 0
# 1 1 0
# 0 0 1
# 0 1
# 输出：
# 0