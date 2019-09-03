## 题目：字符串的排列（68ms）
## 类型：字符串，双指针，划窗（Sliding Window）

## 题目描述：给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。换句话说，第一个字符串的排列之一是第二个字符串的子串。
## 输入：s1 = "ab", s2 = "eidbaooo"
## 输出：True
## 输入：s1 = "ab", s2 = "eidboaoo"
## 输出：False

## 核心：全排列+滑动窗口
## 思路：首先对s1进行全排列，生成一份数组，然后利用滑窗，控制长度为len(s1)的窗口在s2中从头到尾滑动，判断窗口内的函数是否在全排列列表中。
# 参考：https://leetcode-cn.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ 滑动窗口：判断是否包含排列（相当于双指针）
        """
        result = []
        Arr = list(s1)
        if Arr:
            self.Permutation(0, Arr, result)
        print(result)
        size = len(s1)
        for low in range(len(s2)-size):
            high = low + (size-1)
            subS = s2[low:high+1]
            if subS in result:
                return True
        return False

    def Permutation(self, i, Arr, result):
        """ DFS：字符串全排列，i可以理解为第i层
        """
        if i==len(Arr)-1:
            temp = ''.join(Arr)
            result.append(temp)
        else:
            for j in range(i, len(Arr)):
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])
                self.Permutation(i+1, Arr, result)
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])

if __name__ == "__main__":
    s1= "ab"
    s2 = "eidbaooo"
    a = Solution()
    print(a.checkInclusion(s1, s2))


## 测试用例：
# 输入：s1 = "ab", s2 = "eidbaooo"
# 输出：True
# 输入：s1 = "ab", s2 = "eidboaoo"
# 输出：False
