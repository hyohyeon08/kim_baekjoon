def solution(num_list):
    jjaa = 0
    hole = 0
    for i in num_list:
        if(i % 2 == 0):
            jjaa += 1
        else:
            hole += 1
    return [jjaa, hole]