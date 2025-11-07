from string_utils import split_before_each_uppercases

def test_split_before_each_uppercases():
    # Test 1: Normal chemical formula with uppercase letters
    formula = "H2OCO2NH3"
    result = split_before_each_uppercases(formula)
    assert result == ['H2', 'O', 'C', 'O2', 'N', 'H3'], f"Test 1 Failed: {result}"

    # Test 2: Single part formula with no uppercase letters
    formula = "water"
    result = split_before_each_uppercases(formula)
    assert result == ['water'], f"Test 2 Failed: {result}"

    # Test 3: Formula starting with an uppercase letter
    formula = "NaCl2Fe"
    result = split_before_each_uppercases(formula)
    assert result == ['Na', 'Cl2','Fe'], f"Test 3 Failed: {result}"

    # Test 4: Formula with multiple uppercase letters together
    formula = "C6H12O6B"
    result = split_before_each_uppercases(formula)
    assert result == ['C6', 'H12', 'O6', 'B'], f"Test 4 Failed: {result}"

    # Test 5: Empty string
    formula = ""
    result = split_before_each_uppercases(formula)
    assert result == [], f"Test 5 Failed: {result}"

    print("All tests passed!")
