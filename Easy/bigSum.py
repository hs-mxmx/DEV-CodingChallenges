

def bigSum(count,arr):
    result = 0
    for number in arr:
        result += number
    return result


if  __name__ == "__main__":
    arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    count = len(arr)
    result = bigSum(count,arr)