#!/usr/bin/env python3

def main():
    try:
        n1 = int(input("Give me the first number: ").strip())
        n2 = int(input("Give me the second number: ").strip())
        
        print("Thank you!")
        
        print(f"{n1} + {n2} = {n1 + n2}")
        print(f"{n1} - {n2} = {n1 - n2}")
        print(f"{n1} / {n2} = {int(n1 / n2)}")
        print(f"{n1} * {n2} = {n1 * n2}")
        
    except (ValueError, ZeroDivisionError, EOFError):
        pass

if __name__ == "__main__":
    main()
