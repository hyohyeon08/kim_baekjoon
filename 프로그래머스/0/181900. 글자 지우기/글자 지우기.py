def solution(my_string, indices):
    my_string = list(my_string)
    indices.sort()
    indices.reverse()
    for i in indices:
        del my_string[i]
    return ''.join(my_string)