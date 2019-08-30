## 题目: 全量字符集和已占用字符集
## 类型:字符串,字典
## 应用领域：

## 题目描述：给出一个字符串，如A:3,b:5,c:2@a:1,b:2，@前面的称为全量字符集，后面的称为已占用字符集，我们需要获取全量字符集减去已占用字符集之后的字符集。如果@后面不存在已占用字符集，则@也需要保留
## 核心：
## 思路：首先将字符串拆分为两份字符集，然后建立全量字符集和已占用字符集中每个字符的哈希映射，

## 其他知识点: python中对字符串的大小写字母进行转换的方法未swapcase(), 语法: str.swapcase(), 例如, "a".swapcase(), 将输出"A";
# lower能将大写字符转变为小写, 例如:"A".lower(),输出未"a";  upper()能将小写字符转变为大写,例如: "b".upper(),输出为"B""

def characterSet_reduction(a):
    whole_string, haved_string = a.split("@")
    whole_string_list = whole_string.split(",")
    haved_string_list = haved_string.split(",")

    if len(haved_string)>0:
        whole_dict = {}
        for value in whole_string_list:
            a = value.split(":")
            whole_dict[a[0]] = a[1]

        haved_dict = {}
        for value2 in haved_string_list:
            b = value2.split(":")
            haved_dict[b[0]] = b[1]

        whole_dict_new = {}
        for name,number in whole_dict.items():
            if name in haved_dict:
                if int(number) - int(haved_dict[name]) > 0:
                    reduction = str((int(number) - int(haved_dict[name])))
                    whole_dict_new[name] = reduction
            else:
                whole_dict_new[name] = number
        res = []
        for name,number in whole_dict_new.items():
            res.append(name+":"+number)
        return ",".join(res)
    else:
        return a

if __name__ == "__main__":
    a = input()
    res = characterSet_reduction(a)
    print(res)

## 测试用例:
# 输入: A:3,b:5,c:2@a:1,b:2
# 输出: A:3,b:3,c:2
# 输入: a:3,b:5,c:2@
# 输出: a:3,b:5,c:2@
# 输入: a:3,b:5,c:2@a:1,b:2,d:3
# 输出: a:2,b:3,c:2
# 输入: a:3,b:5,c:2@a:1,b:6
# 输出: a:2,c:2
# 输入: b:5,a:3,c:2@a:1,b:2
# 输出: b:3,a:2,c:2

