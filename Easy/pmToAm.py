
actualTime = "12:45:54PM"

hour = int(actualTime[:2])
if hour < 12 and hour > 00:
    if actualTime[-2:] == "PM":
        hour += 12
    else:
        hour = "0" + str(hour)
elif hour == 12 and actualTime[-2:] == "AM":
    hour = "00"

actualTime = actualTime[2:]

result = str(hour) + actualTime 
result = result[:-2]
print(result)
