## 题目：自动校对程序（校正拼写错误）
## 类型：字符串（主要是字符串比较）
## 题目描述：
#  1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
# 2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
# 3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC 

# 思路：建立一个数组，将正确的字母留到数组中，然后对比之后的元素与该数组中元素的最后几位。如果符合错误条件，则过滤掉，否则添加在数组中。

class Solution:
    def autoCheck(self, s):
        res = []
        for elem in s:
            if len(res)>=2:
                if elem == res[-1] and elem == res[-2]:
                    continue
            if len(res)>=3:
                if elem == res[-1] and res[-2] == res[-3]:
                    continue
            res.append(elem)
        return res

if __name__ == "__main__":
    a = Solution()
    n = int(input())
    for i in range(n):
        s = input()
        res = a.autoCheck(s)
        print("".join(res))

## 测试用例：
# 输入：
# 2
# helloo
# woooooow
# 输出：
# hello
# woow
