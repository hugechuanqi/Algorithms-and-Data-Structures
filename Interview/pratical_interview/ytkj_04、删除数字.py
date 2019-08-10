

T = int(input())
for i in range(T):
        print("Case #%d:" %(i+1))
        n = int(input())
        string_ = input()
        a = []
        for k in range(n):
            sum_ = 0
            for j in range(1,len(string_)):
                sum_ = sum_ + int(string_[j]^ string_[j-1])
            if sum_ <= k:
                a.append(k)
        print(" ".join(a))
