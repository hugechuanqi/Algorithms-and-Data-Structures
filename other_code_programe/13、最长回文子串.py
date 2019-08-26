## 题目：最长回文子串
## 类型：数组，回文算法
## 作用：计算回文半径

## 题目描述：

## 思路：


class Solution:
    """ Brute-force暴力求解法
    """
    def shrinkCheckPalindrome(self, s, low, high):
        """ 判断传递的序列是否为回文序列，s[low:high+1]
        """
        while(low<=high):
            if s[low] == s[high]:
                low += 1    #内缩
                high -= 1
            else:
                return False
        return True

    def longestPalindrome(self, s):
        """ 暴力法解回文子串，实际上是滑动窗口，O(n^3)，由于是滑动，因此找的就是最长子串
        """
        for  size in range(len(s),-1,-1):   # 因为作为步长，所以时从length~0
            print(len(s),size)
            for low in range(len(s)):
                high = low + (size-1)   # 以size-1为步长
                if high<len(s):
                    # print(low,high, s[low:high+1])
                    if self.shrinkCheckPalindrome(s, low, high):
                        return s[low:high+1]
        return s[0]


class Solution2:
    """ Brute-force改进，中心外扩法——局部函数，输出所有回文序列，取最长即可
    """
    def expandCheckPalindrome(self, s, low, high):
        """ 从中心点向外扩散，利用回文子串的中心对称性，复杂度O(n^2)，直接返回所有的回文子串，不做判断处理
        """
        while(low>=0 and high<len(s)):  #符合边界限制
            if s[low]==s[high]:
                low -= 1    #外扩
                high += 1
            else:   # 当不满足时，说明当前不符合但上一阶段符合
                return s[low+1:(high-1)+1]
        return s[low+1:(high-1)+1]

    def longestPalindrome(self, s):
        """ 以每个字符串为中心位置外扩，需要考虑单核'aba'，也需要考虑双核'abba'
        """
        if len(s)==1:
            return s
        res = []
        for i in range(len(s)-1):
            res.append(self.expandCheckPalindrome(s, i, i))     # 判断单核'aba'
            dobulePalindrom = self.expandCheckPalindrome(s,i,i+1)
            if len(dobulePalindrom)>=1:
                res.append(dobulePalindrom)     # 判断双核'abba'
        print(res)

        # 计算所有回文子串中的最长回文子串（不重要）
        max_length = 0
        maxValue = ''
        for elem in res:
            if len(elem)>max_length:
                max_length = len(elem)
                maxValue = elem
        return maxValue

class Solution3:
    """ 中心外扩法——公有变量不断被最长回文子串覆盖
    """
    def __init__(self):
        self.maxLength = 0
        self.res = ''

    def expandCheckPalindrome(self, s, low, high):
        """ 从中心点向外扩散，利用回文子串的中心对称性，复杂度O(n^2)，存储最长的回文子串到全局变量res中，并不断覆盖
        """
        while(low>=0 and high<=len(s)-1):
            if s[low]==s[high]:
                if (high-low+1>self.maxLength):     # 不管是否为最大长度，都得不断向外扩，直到不相等
                    self.maxLength = high-low+1
                    self.res = s[low:high+1]
                low -= 1
                high += 1
            else:
                return

    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        for i in range(len(s)-1):
            self.expandCheckPalindrome(s, i, i)
            self.expandCheckPalindrome(s, i, i+1)
            # print(i, self.res)
        return self.res

class Solution4:
    """ Manacher算法——马拉车算法（解决回文子串长度奇偶性不确定造成的不同性质的对称轴位置）
    """
    def manacher(self, s):
        s = '#' + '#'.join(s) + '#'
        # print(len(s), s)

        RL = [0]*len(s)     # 回文半径数组
        MaxRight = 0        # 表示当前访问到的所有回文子串，所能触及到的最右一个字符的位置。
        pos = 0                    # MaxRight对应的回文串地对称轴的位置
        MaxLen = 0          
        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i] = 1
            while(i-RL[i]>=0 and i+RL[i]<len(s) and  s[i-RL[i]]==s[i+RL[i]]):
                    RL[i] += 1

            if RL[i]+i-1>MaxRight:
                MaxRight = RL[i] + i -1
                pos = i
            MaxLen = max(MaxLen, RL[i])     #最大子串长度
        
        i_res = RL.index(max(RL))
        s_res = s[i_res-(RL[i_res]-1):i_res+RL[i_res]]
        return s_res.replace('#', '')   #返回最长子串


if __name__ == "__main__":
    Arr = "hjhijhildhabcbajugfaddhdda"
    a = Solution4()
    # res = a.longestPalindrome(Arr)
    res = a.manacher(Arr)
    print(res)


## 输出的回文子串包括：
# ['h', 'hjh', 'h', 'i', 'j', 'h', 'i', 'l', 'd', 'h', 'a', 'b', 'abcba', 'b', 'a', 'j', 'u', 'g', 'f', 'a', 'd', 'dd', 'd', 'addhdda', 'd', 'dd', 'd']

