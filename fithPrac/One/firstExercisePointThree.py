class raises:
    def __init__(self, exception):
        self.exception = exception
        self.exc_info = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            raise AssertionError(f"{self.exception.__name__} not raised")
        if not issubclass(exc_type, self.exception):
            return False
        self.exc_info = (exc_type, exc_val, exc_tb)
        return True

    def __call__(self, func, *args, **kwargs):
        with self:
            func(*args, **kwargs)


def my_function(arg):
    if arg == "invalid argument":
        raise ValueError("invalid argument is invalid")
    else:
        return arg.upper()

def test_my_function():
    # Test valid argument
    arg = "hello"
    expected_output = "HELLO"
    assert my_function(arg) == expected_output

    # Test invalid argument
    arg = "invalid argument"
    with raises(ValueError) as e:
        my_function(arg)
    assert str(e.value) == "invalid argument is invalid"

