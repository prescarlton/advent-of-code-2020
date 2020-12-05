'''
AOC 2020
Day 1/part 2
Author: Preston Carlton
https://www.github.com/prescarlton/advent-of-code-2020

See README.md for summary

'''


def main():
    # define list to contain all expenses
    expense_report = []
    with open('day1.txt', 'r') as f:
        for line in f.readlines():
            expense_report.append(int(line))

    # cyclomatic complexity: 1billion
    for i in expense_report:
        for j in expense_report:
            if i+j < 2020:
                for k in expense_report:
                    if i+j+k == 2020:
                        print('num1:',i)
                        print('num2:',j)
                        print('num3:',k)
                        print('answer:',i*j*k)
                        return

if __name__ == "__main__":
    main()