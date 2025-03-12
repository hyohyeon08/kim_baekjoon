def solution(food):
    answer = "0"
    re = []
    for i in range(1, len(food)):
        if(food[i] % 2 == 0):
            conunt = (food[i])//2
            re.append(str(i)* conunt)
        else:
            conunt = (food[i]-1)//2
            re.append(str(i)* conunt)
    for i in range(len(re)):
        answer = re[len(re)-1-i] + answer + re[len(re)-1-i]
    return answer