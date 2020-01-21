MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

def MorseDecoder(morse_code):
    morse_decode = ""
    morse_list = []
    solution_list = []
    morse_code = morse_code.upper()
    count = 0
    spaces = 0 

    for character in morse_code:
        count += 1
        if (character != " "):
            morse_decode += character
        if(character == " " or count == len(morse_code)):
            morse_list.append(morse_decode)
            morse_decode = ""

    for word in morse_list:
        if word == "" and spaces == 0:
            print(" ")
            solution_list.append(word)
            spaces+=1
        else:
            spaces = 0
        for k,v in MORSE_CODE_DICT.items():
            if word == v:
                solution_list.append(k)
    
    for word in solution_list:
        if(word == ""):
            morse_decode += " "

        morse_decode += word
    return morse_decode



MorseDecoder(".... . -.--   .--- ..- -.. .   ....")
   
