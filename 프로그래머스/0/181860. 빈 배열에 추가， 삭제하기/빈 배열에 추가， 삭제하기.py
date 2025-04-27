def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if(flag[i]):
            answer.extend([arr[i] for _ in range(arr[i]*2)])
        else:
            [answer.pop() for _ in range(arr[i])]
    
    return answer