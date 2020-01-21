def friend(sentence):
    array = []
    for word in sentence: 
        if len(word)==5: array.append(word)
    return array
        
    
'''
    x: list of strings/people
    returns: list of people with only 4 letters in their names
    '''
    # return [n for n in x if len(n) == 4]