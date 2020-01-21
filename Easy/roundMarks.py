

"""

• Less than 40 is FAIL
• Marks are evaluable if more than 40
• Result calculated with next multiple of 5
• Examples:
    - 38 is fail, rounded to 40
    - 48 is fail, but rounded, 50-48 < 3
    - 47 is fail, but not rounded, 50 - 47 >= 3
    - 57 is passed, 60 - 57 >= 3, so not rounded

"""

def roundMarks(arr):
    result_arr = []
    fail = False
    for num in arr:
        if num < 38: fail = True
        next_mult = int((num / 5) + 1)
        if next_mult*5 - num < 3 and fail == False:
            print(next_mult*5 , "-", num)
            num = next_mult*5
        result_arr.append(num)
        fail = False
    print(result_arr)
        



arr = [73,67,38,33]
roundMarks(arr)