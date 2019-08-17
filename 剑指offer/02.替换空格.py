# -*- coding:utf-8 -*-
## 扩展，除了考虑将空格转化为%20，还可以考虑将不同的汉字转换为特殊字符。——完成，例如Solution.replaceSpace2(s,map_dict)，但是必须事先建立好映射表

class Solution:
    def replaceSpace(self, s):
        """ 替换空格为%20
        """
        return s.replace(' ', '%20')

    def replaceSpace2(self, s, map_dict):
        """ 替换字典中出现的key为其value
        """
        for key,value in map_dict.items():
            s = s.replace(key, value)
        return s

    def replaceSpace3(self, strs):
        """ 一般C++操作形式
        """
        i = 0
        length_new = 0
        while(i<len(strs)):
            if strs[i] == ' ':
                length_new += 3
            else:
                length_new += 1
            i = i + 1
        
        strs_new = [0]*length_new
        j = 1
        length = len(strs)
        while(length>0):
            if strs[length-1]==' ':
                strs_new[length_new-j] = '0'
                strs_new[length_new-j-1] = '2'
                strs_new[length_new-j-2] = '%'
                j = j+3
            else:
                strs_new[length_new-j] = strs[length-1]
                j = j+1
            length -= 1
        return ''.join(strs_new)

if __name__ == "__main__":
    # 测试用例，s为源字符串，
    s = 'We Are Happy'
    a = Solution()
    print(a.replaceSpace(s))

    s1 = 'We 在 博客园 blog'
    map_dict = {" ": "%20",  "在":"%35", "博": "%36", "客": "%37", "园": "%38"}
    a = Solution()
    print(a.replaceSpace2(s1, map_dict))

    s3 = 'We Are Happy'
    a = Solution()
    print(a.replaceSpace3(s3))