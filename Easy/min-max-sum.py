

arr = [1,2,3,4,5]

max_num = 0
min_num = 0

arr.sort()
for n in range(len(arr)-1,len(arr)-5,-1):
    max_num += arr[n]

for n in range(len(arr)-5,len(arr)-1):
    min_num += arr[n]


print(max_num, min_num)