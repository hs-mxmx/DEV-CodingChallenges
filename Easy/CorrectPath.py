
word = "lulululurrrddd??????????"
#word = "rrrrdddd????"
import random
import sys
import os

class CorrectPath:

    def __init__(self):
        self.total_u=0
        self.total_r=0
        self.total_d=0
        self.total_l=0
        self.sol_u=0
        self.sol_r=0
        self.sol_d=0
        self.sol_l=0
        self.total_unknown=0

    def CorrectPath(self,str):
        
        for i in range(0,len(str)):
            if(str[i]=="u"):
                self.total_u+=1
            elif(str[i]=="r"):
                self.total_r+=1
            elif(str[i]=="d"):
                self.total_d+=1
            elif(str[i]=="l"):
                self.total_l+=1
            elif(str[i]=="?"):
                self.total_unknown +=1
            
        if(self.checkTotal()):

            sol_d_check = self.checkPosibilities(self.total_d, self.total_u, 0)
            sol_r_check = self.checkPosibilities(self.total_r, self.total_l, 0)
            sol_u_check = self.checkOthersPositilities(self.total_u, self.total_d, 0)
            sol_l_check = self.checkOthersPositilities(self.total_l, self.total_r, 0)

            self.sol_d = self.sol_d + sol_d_check
            self.sol_r = self.sol_r + sol_r_check
            self.sol_u = self.sol_u + sol_u_check
            self.sol_l = self.sol_l + sol_l_check

            if(self.total_unknown > 0):
                print("Invalid word")
                
            else:
                print("\n\n[-]Word: " + str + "\n")
                print("\t[Counted] \n")
                print("  [-] Total u: " , self.total_u)
                print("  [-] Total d: " , self.total_d)
                print("  [-] Total r: " , self.total_r)
                print("  [-] Total l: " , self.total_l)
                print("  [-] Total ?: " , self.total_unknown)
                print("\n")
                print("\t[Result] \n")
                self.checkPrint("d",self.sol_d)
                self.checkPrint("r",self.sol_r)
                self.checkPrint("u",self.sol_u)
                self.checkPrint("l",self.sol_l)
                print("\n")
        else:
            print("Invalid word...\n")


    def checkTotal(self):
        if(self.total_unknown == 0 and self.total_d == 0 and self.total_r == 0):
            return False
        while(self.total_d == 4 and self.total_r == 4 and self.total_unknown > 0):
            if(self.total_unknown >= 2):
                rand = random.randint(0,1)
                if(rand==0):
                    self.sol_u +=1
                    self.sol_d +=1
                    self.total_unknown -=2
                else:
                    self.sol_l += 1
                    self.sol_r +=1
                    self.total_unknown -=2
            elif(self.total_unknown == 1):
                return False
        if(self.total_d == 0 and self.total_r == 0 and(self.total_l + self.total_u != self.total_unknown)):
            return False
        return True


    def checkPosibilities(self,total_a, total_b, sol_a):
        while(total_a<4 or total_b>0):
            if(total_b>0):
                total_a-=1
                total_b-=1
            else:
                sol_a+=1
                total_a+=1
                self.total_unknown-=1

        return sol_a

    def checkOthersPositilities(self,total_a, total_b, sol_a):
        while(total_b>4):
            if(total_a>0):
                total_a-=1
                total_b-=1
            else:
                sol_a+=1
                total_b-=1
                self.total_unknown-=1
        return sol_a

    def checkPrint(self,word, total):
        if("d" in word):
            print("  [+] Total d: " , total)
        if("u" in word):
            print("  [+] Total u: " , total)
        if("l" in word):
            print("  [+] Total l: " , total)
        if("r" in word):
            print("  [+] Total r: " , total)
        
    '''
    def generateWords(self,number):
        letters = ["d","u","l","r","?"]
        for x in range(0,number):
            word = ""
            for i in range(1,random.randint(0,5)+5):
            rand = random.randint(0,4)
            word+=letters[rand]
            CorrectPath(word)
        sys.exit(1)
    def ChooseOption():
        option1 = "(1) Input word "
        option2 = "(2) Random words "
        example = "(Example): word: ???rlrlddr?"
        option = input("\n" + option1 + "\n" + option2 + "\n\n" + example+ "\n\n\n Option: ") 
        if("1" in option):
            word = input("\n Type your word: ")
            CorrectPath(word)
        elif("2" in option):
            total = input("How many words do you want to generate: ")
            generateWords(int(total))
        else:
            os.system('cls')
            ChooseOption()
    '''

os.system('cls')
Path = CorrectPath()
Path.CorrectPath(word)
