def solution(number):
    result = 0
    for i in range (1,number):
        if(i%3==0 or i%5==0):
            result += i

    return result


print(solution(20))


#def solution(number):
    #return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)