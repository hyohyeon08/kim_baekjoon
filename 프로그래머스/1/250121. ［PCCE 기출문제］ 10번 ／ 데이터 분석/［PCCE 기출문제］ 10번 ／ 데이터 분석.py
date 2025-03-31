def solution(data, ext, val_ext, sort_by):
    sa = {'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3}
    result = [i for i in data if i[sa[ext]] < val_ext]

    result.sort(key=lambda x: x[sa[sort_by]])

    return result