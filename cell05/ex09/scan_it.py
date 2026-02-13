#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) == 3:
        keyword = sys.argv[1]
        search_string = sys.argv[2]
        
        matches = re.findall(keyword, search_string)
        
        if matches:
            print(len(matches))
        else:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    main()
