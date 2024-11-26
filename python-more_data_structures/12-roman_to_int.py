#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    if not isinstance(roman_string, str):
        return 0
    
    total = 0
    length = len(roman_string)
    
    for i in range(length):
        current_value = roman_dict[roman_string[i]]
       
        if i + 1 < length and current_value < roman_dict[roman_string[i + 1]]:
            total -= current_value
        else:
            total += current_value
    
    return total