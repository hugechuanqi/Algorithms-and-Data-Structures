class Solution:
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
        num ='0'
        res = ''
        for elem in s:
            if '0' <= elem <= '9':
                num = num + elem
            elif 'a' <= elem <= 'z' or 'A' <= elem <= 'Z':
                res = res + elem
            elif elem == "[":
                nums.append(num)
                num = '0'
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
