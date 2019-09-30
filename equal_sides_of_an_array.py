def find_even_index(arr):
    #your code here
    index = 0
    for n in arr:
        tmp1 = sum(arr[0:index])
        tmp2 = sum(arr[index+1:])
        if tmp1 == tmp2:
            return index
        else:
            index = index+1
    return -1

arr1 = {20,10,-80,10,10,15,35}

find_even_index(arr1)