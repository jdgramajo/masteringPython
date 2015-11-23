from pkgutil import get_data

def a_func():
    print("Function in module A")

def a_extract_config():
    return get_data(__package__, "data/config_file.txt").decode("utf-8")
