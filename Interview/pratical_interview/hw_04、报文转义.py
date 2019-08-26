## 题目：报文转义
## 题型：字符串、空格替换

## 思路：就是一个字符串转换的问题，中间还涉及到10进制与16进制之间的转换

## 拓展：尝试使用替换空格的方法反向转义添加

def transform(length, s):
    res = []
    for elem in s:
        if elem == 'A':
            res.append('12')
            res.append('34')
            length += 1
        elif elem == 'B':
            res.append('AB')
            res.append('CD')
            length += 1
        else:
            res.append(elem)
    length = hex(length)[2:]
    res.insert(0, str(length))
    return ' '.join(res)

if __name__ == "__main__":
    arr = list(map(str, input().split()))
    length = int('0x'+arr[0], 16)
    s = arr[1:]
    res = transform(length, s)
    print(res)

## 测试用例：
# 输入：
# 8 1 2 3 4 5 6 A
# 输出：
# 9 1 2 3 4 5 6 12 34
# 输入：
# A 1 2 3 4 5 6 A 8 9 A
# 输出：
# C 1 2 3 4 5 6 12 34 8 9 12 34
# 输入：
# A 1 2 3 4 5 6 A 8 9 B
# 输出：
# C 1 2 3 4 5 6 12 34 8 9 AB CD





