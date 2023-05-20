import deal


@deal.pre(lambda a, b: b != 0)
@deal.post(lambda a, b, result: result == a / b)
@deal.ensure(lambda a, b, result: b != 0 or result is None)
@deal.raises(ZeroDivisionError)
@deal.reason(lambda b: b != 0)
def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    :param a: the numerator
    :param b: the denominator
    :return: the quotient

    :raises ZeroDivisionError: if b is 0
    """
    return a / b


def test_divide_with_contract():
    assert divide(4, 2) == 2.0
    assert divide(1, 0) is None


def test_divide_with_contract_error():
    divide(1, 0)
