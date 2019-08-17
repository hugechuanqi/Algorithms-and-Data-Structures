## 题目：建筑物不同埋伏方案数量
## 类型：链表类问题
## 要求：
# 1. 我们在字节跳动大街的N个建筑中选定3个埋伏地点。
# 2. 为了相互照应，我们决定相距最远的两名特工间的距离不超过D。
# 3. 两个特工不能埋伏在同一地点
# 4. 三个特工是等价的：即同样的位置组合(A, B, C) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用 

## 输入：
# 第一行包含空格分隔的两个数字 N和D(1 ≤ N ≤ 1000000; 1 ≤ D ≤ 1000000)
# 第二行包含N个建筑物的的位置，每个位置用一个整数（取值区间为[0, 1000000]）表示，从小到大排列（将字节跳动大街看做一条数轴）
## 输出：
# 一个数字，表示不同埋伏方案的数量。结果可能溢出，请对 99997867 取模

## 思路：由于需要求取方案数量，因此最好的方法是利用排列组合。此题有个前提，即输入是一个排序好的排列（数组），因此直接利用双指针进行遍历即可。首先指针p从数组头部进行遍历，q指针每次后移适当的距离，控制q指针与p指针的取值距离间隔正好在最大间隔以内，然后得到p指针到q指针之间的数量Number，然后从这些数量中任取2个，然后组合，即c*(c-1)/2。

# coding:utf-8
class Solution:
    def __init__(self):
        self.MOD = 99997867

    def calculate_solution_number(self, N, D, array):
        """ 计算不同埋伏方案数量，通过取出数组中元素满足设定的条件
        """
        count = 0
        for i in range(N):
            a = array[i]    # 埋伏点1
            for j in range(i+1,N):
                if j==i:
                    continue
                b = array[j]    # 埋伏点2
                if abs(a-b)>D:
                    break
                for m in range(i+j, N):
                    if m==i or m==j:
                        continue
                    c = array[m]    # 埋伏点3
                    if abs(b-c)>D or abs(a-c)>D:
                        break
                    count +=1
        return count
    
    ## 标准程序
    def calculate_solution_number2(self, N, D, array):
        """ 动态规划，设定两个指针在最大间隔处，剩余一个指针使用排列组合
        """
        number_list = [0]*N
        j  = 0
        for i in range(2, N):
            while j>=0 and abs(array[j]-array[i])>D:
                j = j + 1
            interval = i - j
            number_list[i] = interval*(interval-1)//2 if interval>=2 else 0
            number_list[i] = number_list[i]%self.MOD
        return sum(number_list)%self.MOD

if __name__ == "__main__":
    N, D = list(map(float, input().split()))
    N = int(N)
    array = list(map(float, input().split()))
    a = Solution()
    count2 = a.calculate_solution_number2(N, D, array)
    print(count2)

## 测试用例：
# 输入：
# 4 3
# 1 2 3 4
# 输出：
# 4
