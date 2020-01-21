
import random


def compareTriplets(a,b):
    result_a = 0
    result_b = 0
    result = []
    for i in range (0,len(a)):
        if a[i] > b[i]:
            result_a += 1
        if a[i] < b[i]:
            result_b += 1
    result.append(result_a)
    result.append(result_b)
    return result



if __name__ == '__main__':
    a = []
    b = []
    for i in range(0,3):
        a.append(random.randint(1,100))
        b.append(random.randint(1,100))
    result = compareTriplets(a,b)
    print(result)