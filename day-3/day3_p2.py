'''
AOC 2020
Day 3/part 2
Author: Preston Carlton
https://www.github.com/prescarlton/advent-of-code-2020

See README.md for summary
'''

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

    # list of diff routes and trees hit on each route
    routes = [
        {
            'x': 1,
            'y': 1,
            'trees':0
        },
        {
            'x': 3,
            'y': 1,
            'trees':0
        },
        {
            'x': 5,
            'y': 1,
            'trees':0
        },
        {
            'x': 7,
            'y': 1,
            'trees':0
        },
        {
            'x': 1,
            'y': 2,
            'trees':0
        }

    ]

    # loop thru diff routes
    for route in routes:
        # set starting x_pos and y_pos
        x_pos = 0
        y_pos = 0
        while y_pos <= len(map_lines)-1:
            line = map_lines[y_pos]
            # if line is too short, add a few to it
            while x_pos > len(line)-1:
                line += line

            # check to see if we hit a tree
            if line[x_pos] == '#':
                route['trees'] += 1

            # each time we go to another line, we need to add proper num to x + y
            x_pos += route['x']
            y_pos += route['y']

        print('trees hit:', route['trees'])

    total = 1
    for route in routes:
        total *= route['trees']
    print('answer:',total)
    
if __name__ == "__main__":
    main()
