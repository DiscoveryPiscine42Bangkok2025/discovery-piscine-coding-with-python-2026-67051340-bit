#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    filtered_list = [x + 2 for x in original_array if x > 5]
    new_set = set(filtered_list)
    
    print(original_array)
    print(new_set)

if __name__ == "__main__":
    main()
