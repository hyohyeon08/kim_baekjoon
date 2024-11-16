def solution(n):
    answer = ''
    su = ['수', '박']
    for i in range(n):
        answer += su[i % 2]
    return answer