target = input()
tmps = []
ans = []
pre = -1
for i in range(len(target)):
    if target[i] == ',' and target[i+1] == '"' and target[i+2] == '"':      #为什么敢让长度超出索引
        continue
    if target[i] == ',':
        tmps.append(target[pre+1:i])
        pre = i
    if i == len(target) - 1:
        tmps.append(target[pre+1:])
for tmp in tmps:
    if '"' in tmp:
        tmp = list(tmp[1:-1])
        i = 0
        a = ''
        while i <len(tmp):
            if tmp[i]!= '"':
                a += tmp[i]
                i+= 1
            elif tmp[i] == '"' and tmp[i+1] == '"':
                a+='"'
                i += 2
        ans.append(a)
    else:
        ans.append(tmp)
print(len(ans))
for i in ans:
    if not i:
        print('--')
    else:
        print(i)