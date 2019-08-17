## 题目：字符串缩写
## 类型：字符串

## 思路：将所有字符（包括空格）当作一个字符串。首先，第一个字符必然是缩写的第一个首字母，加入到res中，然后遍历字符串，每当遇到空格，则可以将空格之后的字符加入到res中。最后将加入到res中的字符连接在一切即可。

class Solution():
    def getStringAbbr(self, strs):
        res = []
        res.append(strs[0])
        for i in range(1:len(strs)):
            if strs[i]!=' ':
                continue
            else:
                res.append(strs[i+1])
        return ''.join(res)  

if __name__ == "__main__":
    strs = input()
    a = Solution()
    abbr = a.getStringAbbr(strs)
    print(abbr)

## 测试用例：
# 输入：
# looks good to me
# 输出：
# lgtm
