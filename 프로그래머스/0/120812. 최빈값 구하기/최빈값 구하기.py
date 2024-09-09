def solution(array):
    s_array = set(array)
    
    ch = 0
    new_arr = [0]

    for i in s_array:
        if(ch < array.count(i)):
            ch = array.count(i)
            new_arr[0] = i
        elif(ch == array.count(i)):
            new_arr[0] = -1
    return new_arr[0]