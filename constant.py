class Constant(object):
    def __init__(self, __val, *, deletable: bool = True) -> None:
        self.val       = __val
        self.deletable = deletable

    def __set_name__(self, owner, name):
        if not hasattr(owner, '__class_constants__'):
            owner.__class_constants__ = {}

        owner.__class_constants__[name] = [self.val, self.deletable]

        def __new__(cls, *args, **kwargs):
            obj = super(owner, cls).__new__(cls)

            obj.__dict__['__constants__'] = {}

            return obj

        def __getattribute__(obj, __name: str):
            try:
                if __name in (constants := object.__getattribute__(obj, '__constants__')):
                    return constants[__name][0]

                if __name in owner.__class_constants__:
                    return owner.__class_constants__[__name][0]
            except AttributeError:
                pass # Not yet initialized by __new__

            return object.__getattribute__(obj, __name)

        def __setattr__(obj, __name: str, __val):
            if isinstance(__val, self.__class__) or __name in obj.__constants__:
                if not __name in obj.__constants__:
                    obj.__constants__[__name] = [__val.val, __val.deletable]
                elif obj.__constants__[__name][0] is None:
                    if __val is not None:
                        obj.__constants__[__name][0] = __val
                else:
                    raise AttributeError(f"You can't change the value of constant: {__name}")

            obj.__dict__[__name] = __val

        def __delattr__(obj, __name: str):
            if __name in obj.__constants__:
                if not obj.__constants__[__name][1]:
                    raise AttributeError(f"Can't delete constant '{__name}'")

                del obj.__constants__[__name]

            del obj.__dict__[__name]

        owner.__new__          = __new__
        owner.__getattribute__ = __getattribute__
        owner.__setattr__      = __setattr__
        owner.__delattr__      = __delattr__


class Eggs(object):
    x = Constant(10)
    e = Constant(11)

    def __init__(self):
        self.y = Constant(11, deletable=False)
        self.z = 12

    def foo(self):
        return self.y


f = Eggs()


print(f.e)