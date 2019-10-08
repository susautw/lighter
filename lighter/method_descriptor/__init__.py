__all__ = ['MethodDescriptor', 'with_descriptor']

MethodDescriptor = with_descriptor = object.__class__

from .method_descriptor import MethodDescriptor, with_descriptor
