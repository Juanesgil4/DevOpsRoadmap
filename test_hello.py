from hello import hello, sum_func


def test_hello():
    assert hello("juan") == "hello juan"


def test_sum():
    assert sum_func(1, 2) == 2
    assert type(sum_func(1, 2)) == int
