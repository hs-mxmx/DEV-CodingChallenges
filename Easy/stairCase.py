
####
####
####
####

   #
  ##
 ###
####


print("\n")
max = 6
min = 0
word = ''
for f in range(max,0,-1):
    for spaces in range(min,max-1):
        print(' ', end='')
    for c in range(min,0,-1):
        print('#', end='')
    min += 1
    print('#')