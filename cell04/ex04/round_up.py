#!/usr/bin/env python3
import math
import sys

def main():
    try:
        val = input("Give me a number: ").strip()
        num = float(val)
        
        print(math.ceil(num))
        
    except (ValueError, EOFError):
        pass

if __name__ == "__main__":
    main()
