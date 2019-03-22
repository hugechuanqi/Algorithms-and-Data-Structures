# -*- coding:utf-8 -*-

class Hanoi:
    def chkStep(self, arr, n):
        # write code here
        if len(arr)!=n:
            return
        self.cur_status = [1]*n #初始状态，所有的圆盘都在左柱上
        self.moves = []
        self.moves.append(self.cur_status[:])
        self.solve(n,1,2,3)

        i=0
        for status in self.moves:
            if arr==status:
                return i
            i += 1
        return -1

    def move(self,n,s1,s2):
        self.cur_status[n-1] = s2
        self.moves.append(self,)