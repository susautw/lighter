from typing import Callable, Type
import inspect


class MethodDescriptor:

    def __init__(self, method: Callable):
        assert isinstance(method, Callable), 'parameter (method) must be a Callable.'
        self.method = method
        self.instance = None
        self.owner = None

    def __call__(self, *args, **kwargs):
        assert self.instance is not None, 'method must bind to an instance first.'
        return (self.method.__get__(self.instance, self.owner))(*args, **kwargs)

    def __get__(self, instance, owner=None):
        self.instance = instance
        self.owner = owner
        return self

    @classmethod
    def get_instance_methods(cls, instance):
        return [
            (method_name, method) for method_name, method in inspect.getmembers(instance) if isinstance(method, cls)
        ]


def with_descriptor(descriptor: Type[MethodDescriptor], *args, **kwargs):
    def inner(method: Callable):
        _args = list(args)
        _args.insert(0, method)
        return descriptor(*_args, **kwargs)
    return inner
