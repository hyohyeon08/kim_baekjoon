def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        c = []
        te = arr[queries[i][0]:queries[i][1] + 1]
        for j in range(len(te)):
            if te[j] > queries[i][2]:
                c.append(te[j])
        if c: 
            answer.append(min(c))
        else:
            answer.append(-1)
    
    return answer
