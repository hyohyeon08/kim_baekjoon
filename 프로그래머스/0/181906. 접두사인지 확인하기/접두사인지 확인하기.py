def solution(my_string, is_prefix):
    answer = 0
    if(len(my_string) >= len(is_prefix)):
        if(my_string[0] == is_prefix[0]):
            for i in range(len(is_prefix)):
                if(my_string[i] == is_prefix[i]):
                    answer = 1
                else:
                    answer = 0
                    break
        else:
            answer = 0
    else:
        answer = 0
    return answer