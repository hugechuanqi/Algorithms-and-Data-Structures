# !~/anaconda3/bin/python
# coding:utf-8
class Solution:
    def VerifySquenceOfBST(self, sequence):    #BST（Binary Search Tree）：二叉搜索树 
        # write code here
        if not sequence:    #将`if sequence==None:`改为`if not sequence:`后，list就不会超出索引了
            return False
        length = len(sequence)
        return self.VerifyBST(sequence, 0, length-1)

    def VerifyBST(self, s, first, last):
        length = len(s)
        if s==None or length<0:
            return False
        rootValue = s[length-1]
        i=0
        while(s[i]<rootValue and i<length-1):
            i = i+1
        j=i
        while(j<length):
            if s[j]<rootValue:
                return False
            elif j==length-1:   #每次判断一定要到数组最后一个点
                return True
            j = j+1

        return self.VerifyBST(s[0,i+1], 0, i) and self.VerifyBST(s[i+1,length-2], i, length-2)

# # -*- coding:utf-8 -*-
# class Solution:
#     def VerifySquenceOfBST(self, sequence):
#         # write code here
#         if not sequence:  #将`if sequence==None:`改为`if not sequence:`后，list就不会超出索引了
#             return False
#         if len(sequence)==1:
#             return True
#         length = len(sequence)
#         rootValue = sequence[-1]
#         i=0
#         while(sequence[i]<rootValue):
#             i = i+1
#         k=i
#         for j in range(i, length-1):
#             if sequence[j]<rootValue:
#                 return False
#         left = True
#         right = True
#         leftS = sequence[:k]
#         rightS = sequence[k:length-1]
#         if len(leftS)>0:
#             left = self.VerifySquenceOfBST(leftS)
#         if len(rightS)>0:
#             right = self.VerifySquenceOfBST(rightS)
        
#         return left and right



# s = [12,34,4,5,6,7,7,74,52,5]   #当s=[]时，必须返回false
s = [1,2,3,5,6,7,4] #此处为二叉搜索树的后序遍历序列
# s = []    #空集为False
a = Solution()
print("是否为二叉后序遍历序列", a.VerifySquenceOfBST(s))
