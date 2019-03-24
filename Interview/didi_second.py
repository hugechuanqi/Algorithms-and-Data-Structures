a = input()
a = a.lower()
b=[]
n=len(a)
for i in range(n):
    if(a[n-1-i] not in b):
        b.append(a[n-1-i])
print(b[-1])