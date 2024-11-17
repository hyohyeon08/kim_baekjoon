def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price*(i+1)
    if(answer <= money):
        answer = 0
    else:
        answer -= money
    return answer