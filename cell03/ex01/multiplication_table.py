#!/usr/bin/env python3

import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
            
        num = int(line.strip())
        
        i = 0
        while i < 10:
            result = i * num
            print(f"{i} x {num} = {result}")
            i += 1
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()
