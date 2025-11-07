from string_utils import split_at_first_digit

def test_split_at_first_digit():
    assert split_at_first_digit("H2") == ("H", 2)
    assert split_at_first_digit("He23") == ("He", 23)
    assert split_at_first_digit("Fe") == ("Fe", 1)
    assert split_at_first_digit("Fe1") == ("Fe", 1)
    assert split_at_first_digit("F") == ("F", 1)
    assert split_at_first_digit("He10000") == ("He", 10000)
    assert split_at_first_digit("Abcde1234") == ("Abcde", 1234)
    assert split_at_first_digit("O2") == ("O", 2)
    print("All tests passed!")
