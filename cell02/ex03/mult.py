#!/usr/bin/env python3

def main():
    try:
        print("Enter the first number:")
        n1 = int(input().strip())
        print("Enter the second number:")
        n2 = int(input().strip())

        result = n1 * n2

        print(f"{n1} x {n2} = {result}")

        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")
        else:
            print("The result is positive and negative.")
            
    except (ValueError, EOFError):
        pass

if __name__ == "__main__":
    main()
