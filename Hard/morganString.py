
w1 = "JACK"
w2 = "DANIEL"
w3 = "ABACABA"
w4 = "ABACABA"

def morganAndString(w1, w2):
    list_w1 = []
    list_w2 = []
    list_result = []
    string = ""
    for char in w1.lower(): list_w1.append(ord(char)-96)
    for char in w2.lower(): list_w2.append(ord(char)-96)

    """ While both lists aren't empty """
    while(len(list_w1)>0 or len(list_w2)>0):

        """Compare Values"""

        """ If any of them is empty """
        if len(list_w1) == 0 or len(list_w2) == 0:
            if len(list_w1) == 0:
                while(len(list_w2)>0):
                        list_result.append(list_w2[0])
                        list_w2.pop(0)  
            elif len(list_w2) == 0:
                while(len(list_w1)>0):
                        list_result.append(list_w1[0])
                        list_w1.pop(0)  
        elif len(list_w1) > 0 and len(list_w2) > 0:

            """ If none is empty """
            # First value of first list lower than second list
            if list_w1[0] < list_w2[0]:
                list_result.append(list_w1[0])
                list_w1.pop(0)

            # First value of second array lower than first list
            elif list_w1[0] > list_w2[0]:
                list_result.append(list_w2[0])
                list_w2.pop(0)

            # Same Values
            elif list_w1[0] == list_w2[0]:
                pos = 1
                total_w1 = 0
                total_w2 = 0

                """ While they have the same value """
                while total_w1 == total_w2 and len(list_w1) > 0 and len(list_w2) > 0:
                    pos = 0

                    # Only one remaining
                    if(len(list_w1) == len(list_w2) and len(list_w1) == 1):
                        list_result.append(list_w1[0])
                        list_result.append(list_w2[0])
                        list_w1.pop(0)
                        list_w2.pop(0)

                    # Check if they are the same
                    elif len(list_w1) == len(list_w2):
                        iguales = True
                        pos = 1
                        while iguales and pos < len(list_w1)-1:
                            if list_w1[pos] != list_w2[pos]:
                                iguales = False
                            else:
                                pos += 1
                        if iguales:
                            list_result.append(list_w1[0])
                            list_w1.pop(0)

                    # Check total sum of each array
                    elif(len(list_w1) > 1 and len(list_w2) > 1):
                        total_w1 += list_w1[pos]
                        total_w2 += list_w2[pos]
                        pos += 1

                    # If only one left
                    elif len(list_w1) == 1:
                        list_result.append(list_w1[0])
                        list_w1.pop(0)

                    # If only one left
                    elif len(list_w2) == 1:
                        list_result.append(list_w2[0])
                        list_w2.pop(0)

                # Case 1st array's value is lower than 2nd array
                if total_w1 < total_w2:
                    list_result.append(list_w1[0])
                    list_w1.pop(0)

                # Case 2nd array's value is lower than 1st array
                elif total_w1 > total_w2:
                    list_result.append(list_w2[0])
                    list_w2.pop(0)


    """ Conversion to String """
    for n in list_result:
        mult = 0
        mult_decimal = 0
        if n >= 10:
            mult_decimal = n/10
            mult = n//10
            dif = round((mult_decimal - mult),2)
            if dif != 0:
                while(dif < 1):
                    dif = int(dif * 10)
            else:
                dif = 0
            final_result = (ord(str(mult))*10 + dif +54)
            final_result = int(str(final_result)[1:])
            final_result = final_result + 30
            string += chr(final_result)
        else:
            string += chr(ord(str(n))+16)

            
    return string

print(morganAndString(w1,w2))
print(morganAndString(w3,w4))