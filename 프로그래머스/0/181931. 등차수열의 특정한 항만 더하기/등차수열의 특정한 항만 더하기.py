def solution(a, d, included):
    answer = []
    for i in range(len(included)):
        if(included[i]):
            answer.append(a)
        a += d
    return sum(answer)