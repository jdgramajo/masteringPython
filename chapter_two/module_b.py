from . import _module_a

def b_func():
    print("Function in module B")

def a_func_from_b():
    _module_a.a_func()
