def solution(slice, n):
    answer = 1
    s = slice
    while True:
        if(n - slice > 0):
            answer += 1
            slice += s
        else:
            break
    return answer