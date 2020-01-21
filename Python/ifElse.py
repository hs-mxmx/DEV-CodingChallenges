

if __name__ == '__main__':
    n = int(input().strip())
    range_number = False
    if(n<=20 and n>=6) and n%2 == 0: range_number=True
    if n%2 == 0 and range_number == False:
        print("Not Weird")
    elif n%2 != 0 or range_number:
        print("Weird")



oddNumbers(4)
oddNumbers(5)
oddNumbers(8)