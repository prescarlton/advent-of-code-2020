'''
AOC 2020
Day 3/part 1
Author: Preston Carlton
https://www.github.com/prescarlton/advent-of-code-2020

See README.md for summary
'''


def main():
    map_lines = []
    with open('day3.txt', 'r') as f:
        for line in f.readlines():
            map_lines.append(line.strip())

    # set starting x_pos and y_pos
    x_pos = 0
    y_pos = 0
    trees_hit = 0
    for line in map_lines:
        while x_pos > len(line)-1:
            line += line
        # check to see if we hit a tree
        if line[x_pos] == '#':
            trees_hit += 1

        # each time we go to another line, we need to add 3 to x and 1 to y
        x_pos += 3
        y_pos +=1 

    print('trees hit:',trees_hit)


if __name__ == "__main__":
    main()
