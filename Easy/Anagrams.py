
#abca
#cbaa
import os

                     # M O D E L  /  S T R U C T U R E   D A T A  /  S O L U T I O N

def Count(word):
    array = []
    letter = []
    min = 1
    total = 0
    for i in range(0,len(word)):
        total = 1

        for x in range(min,len(word)):
            if(word[i]==word[x]):
                total +=1

        if(word[i] not in letter):
            letter.append(word[i])
            result_dict = {"Letter":word[i], "Result": total}
            array.append(result_dict)
        min+=1

    return array



def Check(arr1, arr2):
    anagram = False
    for x in range(0,len(arr1)):
        if(arr1[x] in arr2):
            if(arr2[arr2.index(arr1[x])]["Result"] == arr1[x]["Result"]):
                anagram = True
            else:
                anagram = False
                return anagram
        else:
            anagram = False
            return anagram
    return anagram


                     # P R I N T I N G   M O D E L  /  N O   S O L U T I O N

def Result(arr1, arr2):
    print("\t\tRESULT\n\n")

    if(len(arr1) == len(arr2)):
        for x in range(0,len(arr1)):
            print(" \t " + arr1[x]["Letter"] + " : " + str(arr1[x]["Result"])  + "  <||>  " + arr2[x]["Letter"] + " : " + str(arr2[x]["Result"]))
    else:
        if(len(arr1)<len(arr2)):
            for x in range(0,len(arr1)):
                print(" \t " + arr1[x]["Letter"] + " : " + str(arr1[x]["Result"])  + "  <||>  " + arr2[x]["Letter"] + " : " + str(arr2[x]["Result"]))
        else:
            for x in range(0,len(arr2)):
                print(" \t " + arr1[x]["Letter"] + " : " + str(arr1[x]["Result"])  + "  <||>  " + arr2[x]["Letter"] + " : " + str(arr2[x]["Result"]))


    if(Check(arr1,arr2) == True): 
        print("\n\n\t[+]Both words are anagrams\n")
    else: 
        print("\n\n\t[!] Words are not anagrams \n")


def Anagrams(word1,word2): 
    os.system('cls')
    print("\n [*] First Word: " + word1 + "\n")
    d1 = Count(word1)
    print("\n [*]Second Word: " + word2 + "\n")
    d2 = Count(word2)
    Result(d1,d2)


Anagrams("okefhnwoekfnweokfnwsopefmqkoedfnq","okefhnwoekfnweokfnwsopefmqkoedfnq")

