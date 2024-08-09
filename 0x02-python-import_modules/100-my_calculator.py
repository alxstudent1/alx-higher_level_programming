if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    def main():
        if len(sys.argv) -1 != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            return 1
        else:
            if sys.argv[2] == "+":
                add(int(sys.argv[1]), int(sys.argv[3]))
                return 0
            elif sys.argv[2] == "-":
                sub(int(sys.argv[1]), int(sys.argv[3]))
                return 0
            elif sys.argv[2] == "*":
                mul(int(sys.argv[1]), int(sys.argv[3]))
                return 0
            elif sys.argv[2] == "/":
                div(int(sys.argv[1]), int(sys.argv[3]))
                return 0
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                return 1
    main()