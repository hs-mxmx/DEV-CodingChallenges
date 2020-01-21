"""testing stuff"""



# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 

def square():
    i = 1

    while True:
        yield i*i
        i += 1

for num in square():
    if num > 100:
        break
    print(num)
