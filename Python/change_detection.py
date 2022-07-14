
class change_detection(object):
    def __init__(self, __cls):
        self.__cls  = __cls
        self.states = {}

        for name, value in self.__cls.__dict__.items():
            if not (name.startswith('__') or callable(value)):
                self.states[name] = ["INIT", self.__cls.__dict__[name]]
                self.__dict__[name] = self.__cls.__dict__[name]

        self.setup()

    def __call__(self, *args, **kwargs):
        return self.__cls(*args, **kwargs)

    def setup(self):
        def __getattribute__(obj, name: str):
            if name in self.states:
                return self.create_access_obj(name)

            return object.__getattribute__(obj, name)

        def __getattr__(obj, name: str):
            if name in self.states:
                return self.create_access_obj(name)

            return self.create_access_obj(None)

        def __setattr__(obj, name: str, new_value):
            if not callable(new_value):
                current_state, current_value = self.states.get(name, [1, 1])

                if name not in self.states:
                    self.states[name] = ["INIT", new_value]
                elif current_value != new_value:
                    self.states[name] = ["MOD", new_value]
                elif current_state == "DEL":
                    self.states[name] = ["INIT", new_value]
                elif isinstance(new_value, (int, bool)) and isinstance(current_value, (int, bool)):
                    if new_value.__class__ != current_value.__class__:
                        self.states[name] = ["MOD", new_value]

            obj.__dict__[name] = new_value

        def __delattr__(obj, name: str):
            if name in self.states:
                self.states[name][0] = "DEL"

            try:
                del obj.__dict__[name]
            except:
                delattr(obj.__class__, name)

        self.__cls.__getattribute__ = __getattribute__
        self.__cls.__getattr__      = __getattr__
        self.__cls.__setattr__      = __setattr__
        self.__cls.__delattr__      = __delattr__

    def create_access_obj(self, state_of):
        if state_of is None:
            access_obj = type("Unknown", (), {})()
        elif self.states[state_of][0] != "DEL":
            access_obj = type("AccessMe", (self.states[state_of][1].__class__, ), {})(self.states[state_of][1])

            access_obj.__dict__ = self.states[state_of][1].__dict__
        else:
            access_obj = type("DelAttr", (self.states[state_of][1].__class__,), {})()

        return setattr(access_obj, "get_change", self.states.get(state_of, [""])[0]) or access_obj

