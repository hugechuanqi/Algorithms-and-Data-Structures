## 单行输入输出
#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

## 多行输入输出
#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)


## 题目一：根据队列长度和输入队列，求出输出队列
# 规律：正数第n个数列，则从倒数第n个数开始，从后往前以此输出
#coding=utf-8
import sys

def output_array_main(length, array):
    

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    input_list = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        input_list.append(values)
    length = input_list[0][0]
    array = input_list[1]
    out_array = output_array_main(length, array)
    print(out_array)