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

        # ## 当字符串压缩数字在括号后面时
        # def ReverseDecodeString(self, s):
        #     nums = []
        #     strs = []
        #     num = '0'
        #     for elem in s[::-1]:
        #         if '0' <= elem <= '9':
        #             num = num*10

        #     return res

import time
start_time = time.time()
s="10[a2[c]]b"
sReverse = "b[[c]2a]3"
a = Solution()
ss = a.decodeString2(s)
# ssReverse = a.Re
end_time = time.time()
print(ss, (end_time - start_time)*1000, "ms")
