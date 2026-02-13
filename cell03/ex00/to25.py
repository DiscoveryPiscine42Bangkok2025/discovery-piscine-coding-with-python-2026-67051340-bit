#!/usr/bin/env python3

import sys

def main():
    try:
        print("Enter a number less than 25")
        num = int(input().strip())

        if num > 25:
            print("Error")
        else:
            while num <= 25:
                print(f"Inside the loop, my variable is {num}")
                num += 1
                
    except (ValueError, EOFError):
        pass

if __name__ == "__main__":
    main()
