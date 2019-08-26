## 题目：
## 类型：字符串，暴力法求最长无重复子串

## 题目描述：

## 核心：
## 思路：利用滑动窗口依次判断，然后新建一个数组res，每次将不重复的最长子串添加至其中，如果不重复则最长

class Solution:
    """ 暴力法
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

