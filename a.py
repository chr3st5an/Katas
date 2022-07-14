

class Foo(object):

    def __new__(cls, *args, **kwargs):
        return super(Foo, cls).__new__(cls)

    def __init__(self) -> None:
        pass