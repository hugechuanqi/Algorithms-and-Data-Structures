## 题目：正则匹配检查（27%）
## 类型：字符串

## 题目描述：添加为合法序列的最少操作数



def getSubString(a):
    sMap = {"]":"["}
    stack = []
    for i in range(len(a)):
        if a[i] == "[":
            stack.append(a[i])
        elif a[i] == "]":
            if sMap[a[i]]==stack[-1]:
                stack.pop()
            else:
                stack.append(a[i])
    return len(stack)

if __name__ == "__main__":
    a = input()
    res = getSubString(a)
    print(res)

## 测试用例
# 输入：[[][[
# 输出：3

## 第一题：正则匹配检查（完成）
## 第二题：单词排版（完成）

## 第三题：购买衣服（重要）
# 换季了，小红薯看上许多漂亮的衣服，都想买。但是她预算有限，衣橱大小也有限，希望你帮帮她挑选买哪些。

# 有N件衣服，每件衣服有指定的价格P和价值V（代表小红薯的喜欢程度）

# 每件候选衣服只能买一件，预算B限定了总价格上限，衣橱空间S限定了总件数上限

# 希望选择合适的衣服组合，使总价值尽量大

# 当有多个方案总价值相同时，希望总价格尽量小，总价格也相同时，希望购买件数尽量少