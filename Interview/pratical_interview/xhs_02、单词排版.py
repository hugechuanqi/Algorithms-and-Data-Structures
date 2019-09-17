## 题目：单词排版（完成，考试也已结束）
## 类型：字符串
## 重要度：中等

## 题目描述：薯队长接到一项任务，需要对一段英文单词进行排版，排版时需要满足以下要求：
#     1 每行字符数必须相同，不能超过上限M
#     2 满足1前提下，从上到下，每行应采用贪心方法尽量填入更多的单词
#     3 满足2前提下，每行的长度尽量小
#     4 每行字采用居中对齐，单词之间空1个空格，两边可以用空格填充，两边空格数尽量相等，如果做不到则头部空格数略少

## 思路：首先利用split进行切分，建立一个栈strs，然后对于每一个字符串，如果其与strs中元素的长度的总和length不超过限制limit，则将其加入栈strs中，否则将栈中之前的所有元素弹入结果result中，并将栈strs置空，当前元素重新加入到栈strs中。如此遍历所有字符串，直到结束。

def typeSetting(limit, Arr):
    """ 单词排版
    """
    length = 0
    strs = []
    result = []
    for elem in Arr:
        if len(elem)+length <= limit:
            strs.append(elem)
            length = length + len(elem) + 1
        else:
            result.append(" ".join(strs))
            strs = []
            length = 0
            strs.append(elem)
            length = length + len(elem) + 1
    result.append(" ".join(strs))
    return result
            
if __name__ == "__main__":
    limit = int(input())
    Arr = input().split()
    res = typeSetting(limit, Arr)
    for elem in res:
        kong = (limit-len(elem))//2
        if kong>=2:
            print(" "*kong+elem)
        else:
            print(elem)

## 测试用例：
# 输入：
# 13
# I have a dream Martin Luther King
# 输出：
#   I have a  
# dream Martin
# Luther King
