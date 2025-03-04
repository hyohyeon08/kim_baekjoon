def solution(a, b, n):
    answer = 0

    while n >= a:
        nama = n % a
        n = (n // a) * b
        answer += n
        n += nama
    return answer