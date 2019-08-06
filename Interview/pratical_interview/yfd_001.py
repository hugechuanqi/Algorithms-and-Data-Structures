#解压字符串


C = list(map(int, input().split()))
string_list = []
for i in range(C):
    item = input()
    string_list.append(item)

string_array = [[0]]*C
for i in range(C):
    string_array[i] = []
    for s in string_list[i]:
        string_array[i].append(s)

map_list = {"(":")"}
number = ["0","1","2","3","4","5","6","7","8","9"]

for i in range(C):
    string0 = string_array[i]
    for j in range(len(string0)):
        s = string0[j]
        if s in number:
            a = int(s)
            if s 


