class Solution:
    def replaceSpace(self, s):
        return s.replace(' ', '%20')

# 测试用例，s为源字符串，
s = 'We Are Happy'
a = Solution()
print(a.replaceSpace(s))
