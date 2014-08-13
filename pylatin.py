

__author__ = 'KRao4'
print ('Welcome to the Pig Latin Translator!')

pyg = 'ay'

original = input("Enter a word :")
if len(original) > 0 and original.isalpha() :
    print("Original string " + original)
    word = original.lower()
    first = word[0]
    translated = word[1:len(word)] + first + pyg
    print("translated word is " + translated)
else:
    print ("empty")
