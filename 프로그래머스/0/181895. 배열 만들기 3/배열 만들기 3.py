def solution(arr, intervals):
    answer = []
    for i in range(len(intervals)):
        answer.extend(arr[intervals[i][0]:intervals[i][1]+1])
    return answer