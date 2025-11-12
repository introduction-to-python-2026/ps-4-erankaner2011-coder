def split_before_each_uppercases(formula):
    

def split_at_digit(formula):
    # Step 1: Initialize digit_location
    digit_location = len(formula)  # Assume no digit found initially

    # Step 2: Loop through characters to find the first digit
    for i, char in enumerate(formula):
        if char.isdigit():
            digit_location = i
            break

    # Step 3: Check if a digit was found
    if digit_location == len(formula):  # No digit found
        return formula, 1
    else:
        prefix = formula[:digit_location]
        number = int(formula[digit_location:])
        return prefix, number
    
