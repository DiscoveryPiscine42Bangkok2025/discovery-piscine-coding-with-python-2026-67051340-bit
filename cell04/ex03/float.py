#!/usr/bin/env python3

import sys

def main():
    try:
        val = input("Give me a number: ").strip()
        num = float(val)

        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")

    except (ValueError, EOFError):
        pass

if __name__ == "__main__":
    main()
