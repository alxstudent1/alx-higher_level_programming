#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(f"{0:d}")
    else:
        liste = []
        for i in range(1, len(sys.argv)):
            liste.append(int(sys.argv[i]))
        print(f"{sum(liste)}")