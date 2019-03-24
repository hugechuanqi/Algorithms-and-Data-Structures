#头条第二题，自动校对程序
N = input()
number = []
for i in range(int(N)):
    number.append(input())

def autocheck(N, number_list):
    j = 0
    while N>0:
        length = len(number_list[j])
        number = list(number_list[j])
        i = 0
        while i < length:
            if i+2 < length:
                if number[i]==number[i+1] and number[i+1]==number[i+2]:
                    del number[i+2]
                    break

            if i+3 < length:
                if number[i]==number[i+1] and number[i+2]==number[i+3]:
                    del number[i+3]
                    break
            i = i + 1

        N = N - 1
        j = j + 1

    return number

number_fix = str(autocheck(int(N),number))
for i in range(int(N)):
    print(number_fix[i])