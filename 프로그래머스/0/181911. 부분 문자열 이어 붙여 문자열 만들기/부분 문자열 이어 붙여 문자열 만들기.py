def solution(my_strings, parts):
    answer = ''

    for i in zip(my_strings, parts):
        answer += (i[0][i[1][0]: i[1][1] + 1])
        
    return answer