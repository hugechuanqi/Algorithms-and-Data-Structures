# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []    #栈A
        self.stackB = []    #栈B

    def push(self, node):   #进栈
        # write code here
        return self.stackA.append(node)

    def pop(self):  #出栈
        # return xx
        if self.stackB:     #如果B栈不为空
            return self.stackB.pop()
        elif not self.stackA:       #如果A栈为空
            return None
        else:               #即B栈空，A栈不空
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

## 测试用例
s = ["PSH1","PSH2","PSH3","POP","POP","PSH4","POP","PSH5","POP","POP"]
a = Solution()
a.push(s)
print(a.pop())


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

