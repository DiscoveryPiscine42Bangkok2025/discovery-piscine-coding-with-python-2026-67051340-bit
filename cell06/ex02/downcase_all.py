#!/usr/bin/env python3
import sys

def downcase_it(string_to_convert):
    return string_to_convert.lower()

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        for param in sys.argv[1:]:
            print(downcase_it(param))

if __name__ == "__main__":
    main()
