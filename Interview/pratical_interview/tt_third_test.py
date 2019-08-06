input_a = 4
input_b = [2,2,2,1]

def find_min_num(peaple_num,peaple_list):
    wait_list = list(range(peaple_num))
    given_list = [0 for i in range(peaple_num)]
    wait_index = 0
    while len(wait_list) > 0:
        if wait_index == len(wait_list):
            wait_index = 0
        
        true_index = wait_list[wait_index]
        pre_index = true_index - 1
        late_index = (true_index + 1) % peaple_num
        
        v_p = peaple_list[pre_index]
        v   = peaple_list[true_index]
        v_l = peaple_list[late_index]
        
        if given_list[true_index] == 0:
            if (v_p == v)&(v_l == v):
                given_list[true_index] = 1
                del wait_list[wait_index]
            elif (v_p > v)&(v_l > v):
                given_list[true_index] = 1
                del wait_list[wait_index]
            elif (v_p < v)&(v_l >= v):
                if given_list[pre_index] > 0:
                    given_list[true_index] = 1 + given_list[pre_index]
                    del wait_list[wait_index]
                else:
                    wait_index += 1
            elif (v_p >= v)&(v_l < v):
                if given_list[late_index] > 0:
                    given_list[true_index] = 1 + given_list[late_index]
                    del wait_list[wait_index]
                else:
                    wait_index += 1
            elif (v_p < v)&(v_l < v):
                if (given_list[late_index] > 0) & (given_list[pre_index] > 0):
                    given_list[true_index] = max(given_list[late_index],given_list[pre_index]) + 1
                    del wait_list[wait_index]
                else:
                    wait_index += 1
            else:
                wait_index += 1
    return sum(given_list)
s = int(input())
out = []
for i in range(s):
    input_a = int(input())
    input_b = input()
    input_b = input_b.split()
    input_c = []
    for j in input_b:
        input_c.append(int(j))
    out.append(find_min_num(input_a,input_c))
for i in out:
    print(i)