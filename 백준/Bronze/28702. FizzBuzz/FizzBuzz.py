def FB(num : int):
    if(num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif(num % 3 == 0):
        return "Fizz"
    elif(num % 5 == 0):
        return "Buzz"
    else:
        return num


FizzBuzz = [input() for _ in range(3)]

for i in range(3):
    if(FizzBuzz[i].isdecimal()):
        print(FB(int(FizzBuzz[i]) + 3-i))
        break