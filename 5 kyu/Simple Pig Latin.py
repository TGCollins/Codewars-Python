def pig_it(text):
    words = text.split(' ')
    sentence = ' '    
    for word in words:
        if word in '!.%&?':
            sentence = sentence + word
        else:
            translated_word = word[1:] + word[0] + 'ay'
            sentence = sentence + translated_word + ' '    
    return sentence.strip(' ') 
