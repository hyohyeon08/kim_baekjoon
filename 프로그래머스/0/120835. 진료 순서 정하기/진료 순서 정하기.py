def solution(emergency):
    new_emergency = sorted(emergency, reverse=True)
    answer = []

    for i in range(len(emergency)):
        answer.append(new_emergency.index(emergency[i]) + 1)

    return answer