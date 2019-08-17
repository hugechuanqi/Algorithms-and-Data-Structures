# -*- coding:utf-8 -*-
## 扩展：可以指定位置进行pop，而不用pop所有的栈（与题目实现队列没关系）

class Solution:
    def __init__(self):
        self.stackA = []    #栈A
        self.stackB = []    #栈B
        self.queue = []     #队列

    def push(self, node): 
        """进栈"""
        return self.stackA.extend(node)

    def pop(self): 
        """出栈"""
        if self.stackB:     #如果B栈不为空
            return self.stackB.pop()
        elif not self.stackA:       #如果A栈为空
            return None
        else:               #即B栈空，A栈不空
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            while self.stackB:
                self.queue.append(self.stackB.pop())
            return self.queue

    def pop_value(self, value):
        """ pop某个具体的值
        """
        try:
            position = self.stackA.index(value)
            return self.stackA.pop(position)
        except:
            print("No this value")

if __name__ == "__main__":
    ## 测试用例
    s = ["PSH1","PSH2","PSH3","POP","POP","PSH4","POP","PSH5","POP","POP"]
    a = Solution()
    a.push(s[0:5])
    print(a.pop_value("PSH2"))
    print(a.pop())      ## 生成的队列
    


# # -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
         
#     def push(self, node):
#         # write code here
#     #    if len(self.stack1) == 0:
#      #       while len(self.stack2):
#       #          self.stack1.append(self.stack2.pop())
#         self.stack1.append(node)
         
#     def pop(self):
#         # return xx
#         if not len(self.stack2) == 0:
#             return self.stack2.pop()
#         else:
#             while len(self.stack1) > 0:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()

