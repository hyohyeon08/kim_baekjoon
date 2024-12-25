def solution(s):
    new_s = []

    for i in s:
        new_s.append(i)
        if(len(new_s) == 0 or len(new_s) == 1): pass
        elif(i ==')'):
            new_s.pop()
            new_s.pop()
    if(len(new_s) == 0): return True
    return False