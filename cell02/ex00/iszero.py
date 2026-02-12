#!/usr/bin/env python3

import sys

def main():
    try:
        num = input().strip()
        if num == "0":
            print("This number is equal to zero.")
        else:
            print("This number is different from zero.")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
