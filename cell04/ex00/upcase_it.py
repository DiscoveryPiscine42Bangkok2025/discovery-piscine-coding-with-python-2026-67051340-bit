#!/usr/bin/env python3

import sys

def main():
    try:
        word = input("Give me a word: ").strip()
        print(word.upper())
    except EOFError:
        pass

if __name__ == "__main__":
    main()
