def solution(x):
    score = 0
    for i in range(len(str(x))):
        score += int(str(x)[i])
    return x % score == 0