def solution(survey, choices):
    answer = ""
    s = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    
    for i in range(len(survey)):
        if(choices[i] > 3):
            s[survey[i][1]] += choices[i] - 4
        else:
            s[survey[i][0]] += 4 - choices[i]
            
    li = list(s.items())
    
    for i in range(0, 8, 2):
        if(li[i][1] < li[i+1][1]):

            answer += li[i+1][0]
        else:
            answer += li[i][0]
    
    return answer