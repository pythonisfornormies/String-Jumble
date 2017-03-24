"""
stringjumble.py
Author: Kai Darrow
Credit: http://stackoverflow.com/questions/13978387/how-can-i-get-python-to-print-an-entered-message-backwards
http://stackoverflow.com/questions/9050355/python-using-quotation-marks-inside-quotation-marks
http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
http://stackoverflow.com/questions/34128842/how-to-reverse-the-order-of-the-words-string-using-python

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

a = input("Please enter a string of text (the bigger the better): ")
print('You entered "'+a+'". Now jumble it:')

aa = a[::-1]
aaa = " ".join(a.split(" ")[::-1])
aaaa = " ".join(a.split(" ")[::-1])
aaab = aaaa[::-1]

print(aa)
print(aaa)
print(aaab)