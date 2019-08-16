## 题目：字符串解压
## 类型：栈，深度优先搜索

## 题目描述：给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。


## 输入：s = "3[a]2[bc]" 
## 输出：返回 "aaabcbc"
## 输入：s = "3[a2[c]]"
## 输出：返回 "accaccacc"

## 核心：
## 思路：利用双栈实现，第一个栈A存储数字，另一个栈B存储两个'['之间的字符。首先用临时变量res表示'['之前的字符串，用num存储'['之前的数值，每当遇到'['时，就把res存储在栈B，将num存储至栈A，并将res赋值为''，将num赋值为''，并继续遍历改变res和num的值，每当遇到']'时，就弹出栈B和栈A的栈顶元素，将字符串不断叠加到临时变量res中，依次循环操作，直到遍历结束。

class Solution:
    ## 暂时不作这样的考虑
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack1 = []
        stack2 = []
        cur = 0
        n = len(s)
        ss = ''
        while cur < n:
            c = s[cur]
            oc = ord(c)
            print(c, oc)
            if oc >= 48 and oc <= 57:
                start = cur
                while oc >= 48 and oc <= 57:
                    cur += 1
                    oc = ord(s[cur])
                stack1.append(int(s[start:cur]))
                stack2.append(ss)
                ss = ''
            elif c == ']':
                ss = stack2.pop() + stack1.pop() * ss
            else:
                ss += s[cur]
            cur += 1
        return ss

    ## 当字符串压缩数字在括号前面时
    def decodeString2(self, s):
        nums = []
        strs = []
        num =''
        res = ''
        for elem in s:
            if '0' <= elem <= '9':
                num = num + elem
            elif 'a' <= elem <= 'z' or 'A' <= elem <= 'Z':
                res = res + elem
            elif elem == "[":
                nums.append(num)
                num = ''
                strs.append(res)
                res = ''
            elif elem == "]":
                times = int(nums.pop())
                # print(times, res)
                for i in range(times):          # 字母出现的次数在[]前面，如果出现再后面，可以反向遍历
                    strs[-1] = strs[-1] + res
                res = strs.pop()
        return res 

    ## 当字符串压缩数字在括号后面时
    def ReverseDecodeString(self, s):
        nums = []
        strs = []
        num = ''
        res = ''
        for elem in s[::-1]:
            if '0' <= elem <= '9':
                num = elem + num        # 对于数字，由于反向取字符串，因此需要反向读取数字，例如"13"，我们首先取'3'，然后取'1'，因此需要反向拼接字符串，即elem('1') + num('3') 
            elif 'a' <= elem  <= 'z' or 'A' <= elem <= 'Z':
                res = elem + res 
            elif elem == ']':
                strs.append(res)    #当连续出现两次']'时，则会向栈存储一个空字符
                res = ''
                nums.append(num)
                num = ''
            elif elem == '[':
                times = int(nums.pop())
                for i in range(times):
                    strs[-1] = strs[-1] +res
                res = strs.pop()
        return res

import time
start_time = time.time()
a = Solution()

# s="10[a2[c]d]b"
# ss = a.decodeString2(s)

sReverse = "b[d[c]2]3"
ssReverse = a.ReverseDecodeString(sReverse)
end_time = time.time()
print(ssReverse, (end_time - start_time)*1000, "ms")
