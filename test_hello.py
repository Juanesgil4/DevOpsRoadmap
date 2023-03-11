from hello import hello, sum_func, print_dict


def test_hello():
    assert hello("juan") == "hello juan"


def test_sum():
    assert sum_func(1, 2) == 3
    assert type(sum_func(1, 2)) == int


def test_dict():
    assert type(print_dict(**{"a": 1})) == dict
