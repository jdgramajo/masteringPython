from . import _module_a

def b_func():
    print("Function in module B")

def a_func():
    _module_a.a_func()

def get_package_config():
    return _module_a.a_extract_config()
