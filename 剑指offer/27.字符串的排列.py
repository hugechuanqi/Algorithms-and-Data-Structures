## 题目：字符串的排列（全排列）
## 类型：数组，DFS（相对较难理解的深度优先搜索）

## 题目描述：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
## 输入：abc
## 输出：abc,acb,bac,bca,cab,cba（由于是全排列，因此不包括ab,ac,bc等）

## 核心：深度优先下的交换位置
## 思路：要求整个字符串的全排列，总共分为两步。第一步求所有可能出现再第一个位置的字符，即把第一个字符后面所有的字符交换；第二步固定第一个字符，求后面所有字符的排列。

# -*- coding:utf-8 -*-
class Solution:
    # def Permutation(self, ss):
    #     """ 字符串拼接：字符串全排列
    #     """
    #     if not len(ss):
    #         return []
    #     if len(ss) == 1:
    #         return list(ss)
    #     charList = list(ss) # 将字符串变为列表（字符串不可变，列表可变）
    #     charList.sort(reverse=False)    # reverse=False表示升序，True表示降序
    #     pStr = []
    #     for i in range(len(charList)):
    #         if i > 0 and charList[i] == charList[i-1]:
    #             continue
    #         temp = self.Permutation(ss[:i]+ss[i+1:])
    #         for j in temp:
    #             pStr.append(charList[i]+j)      # 此处只是将i位置的字符单独提取出来，与之后的字符串进行叠加，j表示后面的每一个字符
    #     return pStr

    def Permutation(self, strs):
        """ DFS：字符串全排列（深度优先搜索）
        """
        Arr = list(strs)
        result = []
        if Arr or len(Arr)>0:
            self.perm(0, Arr, result)
        return result
    def perm(self, i, Arr, result):
        if i==len(Arr)-1:
            print(Arr)
            temp = ''.join(Arr)
            result.append(temp)
        else:
            for j in range(i, len(Arr)):
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])     # 对应第i层，即第i个位置，每次可以将所有的字符当作首字母深度搜索
                self.perm(i+1, Arr, result)           # 递归进行全排列，直到i==len(Arr)-1，也就是走到了最后一层（从第0层到len(Arr)-1层）
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])

if __name__ == "__main__":
    strs = 'abc'
    a = Solution()
    res = a.Permutation(strs)
    print(res)

## 测试用例：
# 输入：
# abc
# 输出：
# abc, bac,bca,cab,cba
