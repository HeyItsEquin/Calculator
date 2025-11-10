optable = {
    "+": lambda n1, n2: n1 + n2,
    "-": lambda n1, n2: n1 - n2,
    "*": lambda n1, n2: n1 * n2,
    "/": lambda n1, n2: n1 / n2,
    "^": lambda n1, n2: n1 ** n2,
    "%": lambda n1, n2: n1 // n2,
    "|": lambda n1, n2: n1 | n2,
    "&": lambda n1, n2: n1 & n2
}

def output(str):
    print(f"> {str}")

def main():
    ans = 0
    executed = False
    while True:
        try:
            inp = input("> ")

            if inp == "exit" or inp == "x":
                return
            
            if inp == "ans" or inp == "":
                if executed:
                    output(ans)
                continue

            n1, op, n2 = inp.split(" ", 3)
            if not n1 or not op or not n2:
                print("Invalid input")
            try:
                n1 = int(n1)
                n2 = int(n2)

                if op not in optable:
                    raise ValueError("Invalid operand")

                executed = True
                val = optable[op](n1, n2)
                ans = val

                output(val)
            except Exception as e:
                print(f"Invalid input ({e})")
                return
        except KeyboardInterrupt:
            return

if __name__ == "__main__":
    main()

