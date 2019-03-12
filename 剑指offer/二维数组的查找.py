# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        i = 0    #此处为放在右上角
        j = col - 1
        while i<row and j>=0:    #行增加到最大值row-1，列减小到最小值0
            if(target < array[i][j]):
                j -= 1
            elif(target > array[i][j]):
                i += 1
            else:
                # return True    #代表找到
                return print("找到位置：",(i+1,j+1))
        return False    #代表没找到
        
array = [[1,3,7,9,11],[2,5,8,12,15],[3,6,10,17,21],[4,7,13,19,25],[5,9,18,20,38]]
target = 13
a = Solution()
print(a.Find(target,array))
