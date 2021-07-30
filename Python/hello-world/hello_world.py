#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name is "":
        return str("Hello, World!")
    else:
        return str("Hello, %s!") % name