#!/usr/bin/env python3
import sys

def main():
    try:
        word = input().strip()
        
        print(word.swapcase())
        
    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
