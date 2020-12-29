# Write a Python function to sort the words in a string
# Input: string of words, separated by spaces
# Output: string of words sorted alphabetically
# Do not ignore upper case with lower case
import re
def sort_words(text):
    
    lower_text_list = text.lower().split(" ")
    upper_text_list = text.split(" ")
    upper_text_sorted =[]
    
    lower_text_list.sort()
    
    for lower in lower_text_list:
        for upper in upper_text_list:
            if(lower==upper.lower()):
                if(upper not in upper_text_sorted):
                    upper_text_sorted.append(upper)
        

    
    print('INPUT : {0}'.format(text))
    print('OUTPUT : sorted string list is  {0}'.format( upper_text_sorted))


# # # # # # #

sort_words('ananas ORANGE apple orange ora')