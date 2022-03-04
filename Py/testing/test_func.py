import functions_2 as f


def test_list_of_squares():
    assert f.list_of_squares(6) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

def test_fact():
    assert f.fact(10) == 3628800

def test_vowels():
    assert f.vowels("python") == 1