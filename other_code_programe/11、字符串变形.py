## 题目：字符串变形
## 类型：字符串型

## 题目描述：对于一个给定的字符串，我们需要在线性(也就是O(n))的时间里对它做一些变形。首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把着个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。比如"Hello World"变形后就变成了"wORLD hELLO"。 

## 核心：需要考虑最后一个字符是否为空格字符，如果不是就好说。
## 思路：本题需要完成以空格进行分隔的字符串饭庄，并且实现每个大小写字母的变换。res临时存储空格间的字符串，首先判断最后一个字符是否为空格，如果不是，则直接将临时字符串变量res插入到列表的第一个位置，如果是，则首先将res插入到列表第一个位置，然后插入一个空字符；然后判断剩余的字符，如果遇到空格，则将res插入到列表中，否则转变大小写之后合并到res中。


# -*- coding:utf-8 -*-

class Transform:
    def trans(self, s, n):
        """ 把空格当作一种字符
        """
        strs = []
        res = ''
        for i in range(len(s)):
            elem = s[i]
            if i==n-1:
                if elem!=' ':
                    res += elem.swapcase()
                    strs.insert(0, res)
                    res = ''
                else:
                    strs.insert(0, res)
                    res = ''
                    strs.insert(0, '')
            elif elem==' ':
                strs.insert(0, res)
                res = ''                
            else:   # 剩下的情况就全部都是字符大小写了
                res = res + elem.swapcase()
        return ' '.join(strs)

    def trans2(self, s, n):
        """ 把空格也当作一种字符，倒序输出
        """
        res = ''
        while(n>0):
            if s[n-1]==' ':
                res += s[n-1]
            else:
                res += s[n-1].swapcase()
            n = n - 1
        return res

    def trans3(self, s, n):
        # print(s.split(' '))
        # print(' '.join(s.split(' ')[::-1]))
        return ' '.join(s.split(' ')[::-1]).swapcase()

if __name__ == "__main__":
    s = "This is a sample "
    n = 17
    a = Transform()
    trans_string = a.trans(s, n)
    print(trans_string) 


## 测试用例：
# 输入：
# "This is a sample",17
# 输出：
# " SAMPLE A IS tHIS"



