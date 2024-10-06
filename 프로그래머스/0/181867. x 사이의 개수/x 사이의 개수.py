def solution(myString):
    answer = []
    myString = myString.split("x")
    for i in myString:
        if(i):
            answer.append(len(i))
        else:
            answer.append(0)
    return answer