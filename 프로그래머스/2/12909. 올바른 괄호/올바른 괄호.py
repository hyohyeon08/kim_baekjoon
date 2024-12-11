def solution(s):
    new_s = []

    for i in range(len(s)):
        new_s.append(s[i])
        if(len(new_s) == 0 or len(new_s) == 1): pass
        elif(s[i] ==')'):
            new_s.pop()
            new_s.pop()
    if(len(new_s) == 0): return True
    return False