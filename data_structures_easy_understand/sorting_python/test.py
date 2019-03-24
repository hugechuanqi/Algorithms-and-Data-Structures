def partition(Arr,low,high):
    hp = Arr[high]  #首先以hp为枢轴
    i = low - 1
    for j in range(low,high):
        if Arr[j] < hp:     #把比枢轴小的放到左边，枢轴实际位置就在i+1
            i = i+ 1
            (Arr[i], Arr[j]) = (Arr[j], Arr[i])
    (Arr[i+1], Arr[high]) = (Arr[high],Arr[i+1])    #确定枢轴位置后，再把枢轴值hp换过来
    return i+1  #相当于先把枢轴值放在


def QuickSort(Arr, low, high):
    if low < high:
        pivot = partition(Arr,low,high)
        QuickSort(Arr,low,pivot-1)
        QuickSort(Arr,pivot+1,high)
    return Arr


a = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]
print("排序前：",a)
QuickSort(a,0,len(a)-1)
print("排序后:",a)
