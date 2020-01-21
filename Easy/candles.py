


def cakeBirthday(age, candles):
    total_candles = []
    total_count = 0
    max_num = 0
    candles = candles.replace(' ','')
    for w in candles:
        total_candles.append(int(w))

    
    for n in total_candles:
        if n >= max_num:
            max_num = n

    for n in total_candles:
        if(n == max_num):
            total_count += 1

    print(total_candles)
    print(max_num)
    print(total_count)


cakeBirthday(5,'1 9 8 2 3 4 9 9')