#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
        for index, value in enumerate(argv[1 : ], start=1):
            print("{:d}: {:s}".format(index, value))
    elif len(argv) > 2:
        print("{:d} arguments:".format(len(argv)))
        for index, value in enumerate(argv[1 : ], start=1):
            print("{:d}: {:s}".format(index, value))            
    else:
        print("0 arguments.")
