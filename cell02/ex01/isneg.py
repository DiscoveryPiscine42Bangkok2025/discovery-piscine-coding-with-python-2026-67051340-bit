#!/usr/bin/env python3

import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        
        num = int(line.strip())
        
        if num < 0:
            print("This number is negative.")
        elif num > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
