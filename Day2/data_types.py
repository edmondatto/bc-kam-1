"""
A function that takes one argument, Compares and returns 
results, based on the argument supplied to the function. 
"""


def data_type(arg):
    if arg is not None:
        if isinstance(arg, str):
            return len(arg)
        elif isinstance(arg, bool):
            return arg
        elif isinstance(arg, int):
            if arg < 100:
                return 'less than 100'
            elif arg > 100:
                return 'more than 100'
            else:
                return 'equal to 100'
        elif isinstance(arg, list):
            if len(arg) > 2:
                return arg[2]
            else:
                return None
    else:
        return 'no value'
