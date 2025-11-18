def split_before_each_uppercases(formula):
    t = []
    splited_formula = []
    for char in formula:
        if char.isupper():
            if t:
                splited_formula.append(''.join(t))
            t = [char]
        else:
            t.append(char)
    if t:
        splited_formula.append(''.join(t))
    return splited_formula
def split_at_first_digit(formula):
    digits = []
    letters = []
    for char in formula:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
    if digits == []:
        digits.append("1")
    return ''.join(letters), int(''.join(digits))
