def test_passes():
    assert True

def test_a_bit():
    import random
    a = 1
    b = 2
    di = {'a': [1, 2, 3],
          'b': {'c': [1, 3, 4],
                'd': {}},
          'c': 4}
    rand = random.randint(0, 4)
    assert rand > 2
