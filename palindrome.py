# Write a Python function to determine of a given
# string is a palindrome.
# Input: string to evaluate / Output: Boolean value
# Only consider letters (A-Z)
# Ignore case (for example. 'A'=='a') and symbols. Only alphanumeric equals


def ifPalindrome(example):
    
   if((not isinstance(example,str))):
       raise TypeError
    
#  merge string in one with small letters
   edited_example = example.replace(" ","").casefold()
   example_with_no_symbols = ''
   
#   Remove all symbols from string
   for character in edited_example:
    if character.isalnum():
        example_with_no_symbols += character
        
# Reverse string  
   palindrome = example_with_no_symbols[::-1]
   
   if(palindrome==example_with_no_symbols):
       print(f'Input ( {example} ) is palindrome. Output ( {palindrome} )')
       return True
   else:
       print(f'Input ( {edited_example} ) is not the same as output( {palindrome} )')
       return False
   
   
print(ifPalindrome('Co mi dał duch – cud, ład i moc.'))   