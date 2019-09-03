## 题目：无重复字符最长子串
## 类型：字符串，暴力法求最长无重复子串

## 题目描述：获取无重复最长子串的长度，即子串中的每一个字符都仅出现一次。例如，"abcabcbb"的最长子串为"abc"，长度为3。

## 核心：取最长子串，则滑动窗口应该依次从大到小。
## 思路：利用滑动窗口，从长窗口依次缩小，获取窗口内的字符串，然后新建一个数组res，每次将可能不重复的最长子串添加至其中，如果确实不重复则最长。

class Solution:
    """ 暴力法，滑动窗口
    """
    def checkDuplicate(self, s):
        res = []
        for elem in s:
            if elem not in res:
                res.append(elem)
            else:
                return False
        return True

    def getLongestString(self, strs):
        """ 滑动窗口：获取最长子串
        """
        if len(strs)==0:
            return 0
        if len(strs)==1:
            return 1
        for size in range(len(strs),-1, -1):
            for low in range(len(strs)):
                high = low + (size-1)
                if high<len(strs):
                    s = strs[low:high+1]
                    if  self.checkDuplicate(s):
                        return s

if __name__ == "__main__":
    strs = input()
    a = Solution()
    s = a.getLongestString(strs)
    print(len(s))

## 测试用例：
## 输入：
# abcabcbb
## 输出：
## 3

