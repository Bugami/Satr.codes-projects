# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:00:00 2021

convert number to words challenge

Thanks to Ayoub ABOUNAKIF's code help me to understand how to solve this challenge

Taken the code with slight changes from this article
https://stackoverflow.com/a/51020974

@author: a.bugami
"""

def numToEng(n):
  # write your code here
    one_ten=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
    'eight', 'nine']
    ten_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 
    'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    twenty_ninety=[' ', ' ','twenty', 'thirty', 'forty', 'fifty', 'sixty', 
    'seventy', 'eighty',
    'ninety']
    temp_str = ""
    if n == 0: # If the string given equals to 0
        temp_str = 'zero ' # Assign the word zero to the var temp_str
    # Do the calculation to find each digit of the str given
    second_digit = (n % 1000) // 100
    third_digit = (n % 100) // 10
    fourth_digit = (n % 10)
    # one_ten[first_digit] gets you the number you need from one_ten and you add thousand (since we're trying to convert to words ofc)
    # You do the same for the rest...
    if second_digit > 0:
        temp_str = temp_str + one_ten[second_digit] + ' hundred '
    if third_digit > 1:
        if not fourth_digit:
            temp_str = temp_str + twenty_ninety[third_digit] + " "
        else:
            temp_str = temp_str + twenty_ninety[third_digit] + "-"
    if third_digit == 1:
        temp_str = temp_str + ten_nineteen[fourth_digit] + " "
    else:
        if fourth_digit:
            temp_str = temp_str + one_ten[fourth_digit] + " "
    if temp_str[-1] == " ": # If the last index is a space
        temp_str = temp_str[0:-1] # Slice it 
    return temp_str
    pass
