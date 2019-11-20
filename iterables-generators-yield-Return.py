mylist = [1, 2, 3]  # mylist is an iterable
for i in mylist:
    print(i)

mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

'''
Everything you can use "for... in..." on is an iterable; lists, strings, files...
These iterables are handy because you can read them as much as you wish, but you store all the 
values in memory and this is not always what you want when you have a lot of values.
'''

'''
Generators are iterators, a kind of iterable you can only iterate over once. 
Generators do not store all the values in memory, they generate the values on the fly:
'''
mygenerator = (x*x for x in range(3))  # This results in a generator object , check type of mygenerator
for i in mygenerator:
    print(i)
'''
It is just the same except you used () instead of []. 
BUT, you cannot perform for i in mygenerator a second time since generators can only be used once:
 they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one
'''
def nextSquare():
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)