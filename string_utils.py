def split_before_each_uppercases(formula):
    

def split_at_digit(formula):
    digit_location = len(formula)
    for i, char in enumerate(formula):
        if char.isdigit():
            digit_location = i
            break
    if digit_location == len(formula):
        return formula, 1
    else:
        prefix = formula[:digit_location]
        number = int(formula[digit_location:])
        return prefix, number
    
