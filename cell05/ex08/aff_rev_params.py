#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 3:
        print("none")
    else:
        params = sys.argv[1:]
        for p in reversed(params):
            print(p)

if __name__ == "__main__":
    main()
