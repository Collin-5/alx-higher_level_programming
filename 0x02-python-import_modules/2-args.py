#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    elements = len(arguments)
    if elements == 0:
        print("{} arguments.".format(elements))
    elif elements == 1:
        print("{} argument:".format(elements))
        print("{}: {}".format(elements, arguments[0]))
    else:
        print("{} arguments:".format(elements))
        for i in range(0, elements):
            print("{}: {}".format(i + 1, arguments[i]))
