def solution(nums):
    answer = 0
    new_nums = list(set(nums))
    if(len(nums)//2 > len(new_nums)):
        answer = len(new_nums)
    else:
        answer = len(nums)//2
    return answer