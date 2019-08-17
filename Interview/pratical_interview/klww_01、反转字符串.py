
def transform(strs):
    res = [0]*len(strs)
    name = []
    for i in range(len(strs)):
        if 'a'<=strs[i]<='z' or 'A'<=strs[i]<='Z':
            name.append(strs[i])
        else:
            res[i] = strs[i]
    for i in range(len(res)):
        if res[i]==0:
            res[i] = name.pop()
    return ''.join(res)

if __name__ == "__main__":
    strs = input()
    strs_new = transform(strs)
    print(strs_new)

## 测试用例：
# 输入：
# a,b!rgh%
# 输出：
# h,g!rba%