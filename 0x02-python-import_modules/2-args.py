#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    if argLen == 1:
        print("{} arguments.".format(argLen - 1))
    elif argLen == 2:
        print("{} argument:".format(argLen - 1))
    else:
        print("{} arguments:".format(argLen - 1))
    for j in range(1, argLen):
        print("{}: {}".format(j, sys.argv[i]))

