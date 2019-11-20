"""
Whenever the Python interpreter reads a source file, it does two things:

it sets a few special variables like __name__, and then
it executes all of the code found in the file.

If you are running your module (the source file) as the main program,
the interpreter will assign the hard-coded string "__main__" to the __name__ variable
__name__ = "__main__"

"""


print("before import")
import math

print("before functionA")


def functionA():
    print("Function A")


print("before functionB")


def functionB():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")