
import random


def plusMinus(arr):
    total_neg = 0
    total_pos = 0
    total = 0
    for i in range(0,len(arr)):
        if(arr[i]>0): total_pos += 1
        if(arr[i]==0): total += 1
        if(arr[i]<0): total_neg += 1
    total_pos = total_pos/len(arr)
    total = total/len(arr)
    total_neg = total_neg/len(arr)
    result= [total_pos,total_neg,total]
    for item in result: print(item)
    



if __name__ == '__main__':
    arr = []
    for i in range (0,6): arr.append(random.randint(-100,100))
    print(arr)
    plusMinus(arr)






"""
import random

def plusMinus(arr):
    total = 0
    min = 0 
    seen = []
    result_dict = []
    dict_total = {}
    for i in range(min,len(arr)):
        if arr[i] not in seen:
            seen.append(arr[i])
            for k in range(min,len(arr)):
                if arr[i] == arr[k]:
                    total += 1
            dict_total[total] = len(arr)
            total = 0
    print(dict_total)
    for k,v in dict_total.items():
        result_dict.append(k/v)
    result_dict.sort(reverse=True)
    print(result_dict)
    return result_dict




if __name__ == '__main__':
    a = [-4,3,-9,0,4,1]
    print(a)
    plusMinus(a)
"""