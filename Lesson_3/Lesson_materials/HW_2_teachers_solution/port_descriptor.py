import sys

sys.path.append('../../')

class Port:
    def __init__(self, default) -> None:
        self.__validate_value(default)
        self._default = default
        self._name = None

    def __get__(self, instance, cls):
        return getattr(instance, self._name, self._default)

    def __set__(self, instance, value):
        self.__validate_value(value)
        setattr(instance, self._name, value)

    def __set_name__(self, cls, name):
        self._name = f"__{name}"

    @staticmethod
    def __validate_value(value):
        if not isinstance(value, int):
            raise TypeError(f'value expected to be int, got {type(value)}')

        if not 0 < value <= 65365:
            raise ValueError('Invalid port value')


