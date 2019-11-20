import nameMain
nameMain.functionB()

"""
When Your Module Is Imported By Another code (BOTH THE CODES ARE IN THE SAME LOCATION)
In this case, the interpreter will look at the filename of your module, foo.py, 
strip off the .py, and assign that string to your module's __name__ variable, i.e.
__name__ = "foo"

"""


"""
You can also import your codes in another location, you can use importlib
"""

import importlib, importlib.util


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


__name__ = 'advancedRNN'
strutils = module_from_file("advancedRNN", "/Users/himanshuaggarwal/PycharmProjects/neural-networks/advancedRNN.py")

