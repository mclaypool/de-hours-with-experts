#!/usr/bin/python3
import sys
from itertools import permutations

def main():
    print(next_biggest_number(sys.argv[1]))

def next_biggest_number(num):
    num = int(num) # make sure this is always an int
    num_str = str(num)

    # try the easiest solution first to save time
    if len(num_str) < 2:
        return -1

    # create all the permutations for the input in sorted order
    # gotta love built-in python functions!
    num_lst = sorted(list(num_str))
    perms = permutations(num_lst)

    # loop the permutations until the smallest larger number is found
    for perm in perms:
        next_num = int(''. join(perm))

        # test if its the solution
        if next_num > num:
            return next_num

    # return -1 if a larger number is not found in the loop
    return -1

if __name__ == "__main__":
    main()
