'''
AOC 2020
Day 1/part 1
Author: Preston Carlton
https://www.github.com/prescarlton/advent-of-code-2020

See README.md for summary
'''
import time

def main():
    # define list to contain all expenses
    expense_report = []
    with open('day1.txt', 'r') as f:
        for line in f.readlines():
            expense_report.append(int(line))

    # loop thru all expenses
    for i in expense_report:
        # if this is one number of the pair, then
        # we can find the other number by doing 2020 - i.
        # then, return the product of the two numbers.
        if (2020-i) in expense_report:
            print(f'first num: {i}\nsecond num: {2020-i}')
            print(i*(2020-i))
            return


if __name__ == "__main__":
    main()