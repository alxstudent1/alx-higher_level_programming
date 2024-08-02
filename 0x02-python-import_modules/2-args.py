#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
        for index, value in enumerate(argv[1 : ], start=1):
            print(f"{index}: {value}")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for index, value in enumerate(argv[1 : ], start=1):
            print(f"{index}: {value}")            
    else:
        print("0 arguments.")