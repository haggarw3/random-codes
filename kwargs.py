def args_example(*args):
    print(args)


args_example(1)

args_example(1,2,3,4,5)


def kwargs_example(**kwargs):
    for key, value in kwargs.items():
        # printing the key and value pairs
        print(key + ': ' + value)


kwargs_example(one='1')
kwargs_example(one='1',two='2',three='3',four='4')