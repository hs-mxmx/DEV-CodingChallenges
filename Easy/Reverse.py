
def spin_words(sentence):
    current_string = sentence.split()
    new_string = []
    for word in current_string:
        if len(word) >= 5:
            new_string.append(word[::-1])
        else:
            new_string.append(word)
    return " ".join(new_string)


print(spin_words("Hey fellow warriors"))
    
# return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])