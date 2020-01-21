
import math

def is_square(n):
    if n < 0 :
        return False

    print(math.sqrt(n))
    print(math.sqrt(n)%1)
    if(math.sqrt(n) % 1 == 0):
        return True



print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))