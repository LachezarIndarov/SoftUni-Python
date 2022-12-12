"""
Input1                                                                          Output1

There are so many emoticons nowadays :P. I have many                            :P
ideas :O what input to place here :)                                            :O
                                                                                :)
"""

def emoticon_finder(text):
    result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ':' and text [i + 1] != ' ']
    print('\n'.join(result))


text = input()
emoticon_finder(text)

"""
Variant 2 - With for loop

def imoticona_tarsachka(text):

    for i in range(len(text)):
#        result = text[i] + text[i + 1] 

        if text[i] == ':' and text[i + 1] != ' ': 
            result = text[i] + text[i + 1] 
            print((result))

text = input()  
imoticona_tarsachka(text)

"""