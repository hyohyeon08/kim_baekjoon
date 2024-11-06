def solution(numbers):
    ch = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if(i in ch):
            ch.remove(i)
    return sum(ch)