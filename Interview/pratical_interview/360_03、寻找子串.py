## 题目：寻找子串
## 类型：字符串，字典


## 题目描述：给出一个字符串，让你寻找其中出现次数最多的子串，输出出现次数。例如，字符串'aba'的出现次数最多的子串为'a'，出现两次。
## 思路：由于出现次数最多的多子串必然由多个单字符组成，因此出现子串最多的必然也是单个字符，例如'abdcabab'，可能会想到'ab'出现了三次，应该是最多的，但是'a'和'b'也出现了3次，因此计算'a'的次数就是'ab'的次数，并且假定这个时候又多了个'ac'那么'a'就出现了4次，'a'才是更多的，因此整个过程只需要计算单个字符出现的次数即可。

def getNum(strs):
    count ={}
    for i in set(strs):
        count[i]=strs.count(i)
    return count

if __name__ == "__main__":
    strs=input()
    count = getNum(strs)
    max_value=max(count.values())
    print(max_value)



