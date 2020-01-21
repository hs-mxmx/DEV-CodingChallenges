
import os
import sys


def simpleArraySum(arr):
    result = 0
    for num in arr:
        result += num
    return result


if __name__ == '__main__':
    arr = [1,2,3]
    number = simpleArraySum(arr)
    print(number)