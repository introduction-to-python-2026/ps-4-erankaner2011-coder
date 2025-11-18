def split_before_each_uppercase(sigma):
    start = 0
    split_formula = []
    for end in range(1, len(s)):
        if sigma[end].isupper():
            split_formula.append(sigma[start:end])
            start = end
    split_formula.append(sigma[start:])
    return split_formula

    

def split_at_first_digit(formula):
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
    
