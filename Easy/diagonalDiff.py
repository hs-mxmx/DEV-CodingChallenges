
import random

def matrixCalc(num):
    first = 0
    second = 0
    pos_first = 0
    pos_second = num-1
    A = [[random.randint(1,10) for x in range(num)]for y in range(num)]
    print(A)
    for number in A:
        first += number[pos_first]
        second += number[pos_second]
        pos_first += 1
        pos_second -= 1
    result = abs(first-second)
    return result
    
    



if __name__ == '__main__':
    result = matrixCalc(3)
    print(result)