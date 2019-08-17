## 题目：删除公共字符
## 类型：字符串

## 题目要求：输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”

## 思路：python处理字符串比较方便，可以将字符串中的每个字符当作一个元素，判断即可。首先遍历一次字符串，然后判断该字符串是否在待删除字符串中，如果是删除即可

class Solution:
    def removeString(self, strs, remove_str):
        res = []
        for s in strs:
            if s not in remove_str:
                res.append(s)
        return ''.join(res)

if __name__ == "__main__":
    strs = input()
    remove_str = input()
    a = Solution()
    res = a.removeString(strs, remove_str)
    print(res)

## 测试用例
# 输入：
# They are students. 
# aeiou
# 输出：
# Thy r stdnts.



