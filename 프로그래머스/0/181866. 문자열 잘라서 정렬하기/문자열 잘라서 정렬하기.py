def solution(myString):
    myString = myString.split('x')
    myString = [s for s in myString if s]  # 빈 문자열 제거
    myString.sort()
    return myString
