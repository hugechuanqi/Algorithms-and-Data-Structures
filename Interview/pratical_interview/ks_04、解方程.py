## 题目：
## 类型：数学问题

## 题目描述：求解一元一次方程的正整数解。（字符串保证为20个字符，方程包括+、-、x、=）

## 核心：输出还得是正整数int型，服了。
## 思路：



def solve(eq,var='X'):
    try:
        eq1 = eq.replace("=","-(")+")"
        c = eval(eq1,{var:1j})
        return -c.real/c.imag
    except:
        return -1

if __name__ ==  "__main__":
    eq = input()
    res = solve(eq)
    print(res)