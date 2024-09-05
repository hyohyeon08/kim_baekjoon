def solution(n):
    answer = 0
    new_p = []
    for i in range(1, n+1):
        if(n % i ==0):
            new_p.append(i)
    for j in new_p:
        for k in new_p:
            if(j * k == n):
                answer += 1
    return answer