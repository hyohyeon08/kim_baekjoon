def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    for i in range(len(phone_number)):
        if(i + 4 == len(phone_number)):
            break
        else:
            phone_number[i] = '*'
    for i in phone_number:
        answer += i
    return answer