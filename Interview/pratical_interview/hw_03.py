## 题目: 返回逻辑运算之后的结果
## 类型: 字符串型

# - 核心: 针对正括号和反括号,需要用到后入先出的概念,因此可以使用栈来实现;

def getSubString(a):
    stack = []
    for i in range(len(a)):
        if a[i] == "(":
            stack.append(i)
        elif a[i] == ")":
            right = a[i]
            left = stack.pop()
            flag = Operation_SubString(a[left+1, right-1])
            a = a[0:left] + flag + a[right+1:]

def Operation_SubString(b):
    legalString = ["0", "1", "(", ")", "&", "|", "!"]
    stack = []
    for i in range(len(a)):
        if a[i] ==

a = input()
res = getSubString(a)


