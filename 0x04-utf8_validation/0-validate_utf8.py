#!/usr/bin/python3
''' utf8 Validation '''
binary_rep_for_n = []


def DecimalToBinary(num):
    ''' Converts a decimal number to its bianry representation '''
    if num >= 1:
        DecimalToBinary(num // 2)
    binary_rep_for_n.append(num % 2)
    return (num % 2)


def validUTF8(data):
    ''' determines if a given data set represents a valid UTF-8 encoding '''
    binary_numbers = []
    for num in data:
        del binary_rep_for_n[:]
        DecimalToBinary(num)
        if len(binary_rep_for_n) > 8:
            return False
    return True
