'''
AOC 2020
Day 2/part 1
Author: Preston Carlton
https://www.github.com/prescarlton/advent-of-code-2020

See README.md for summary
'''


def main():
    # create a list of rules and passwords from given list
    passwords = []
    with open('day2.txt', 'r') as password_file:

        for line in password_file.readlines():
            # split line up into parts
            line_parts = line.split(' ')
            # get range of num of occurences needed
            rule_range = line_parts[0]
            rule_range_lower = rule_range.split('-')[0]
            rule_range_upper = rule_range.split('-')[1]
            # get target char
            char = line_parts[1].replace(':', '')
            # get password
            password = line_parts[2]
            # add to password list
            passwords.append({
                'range': {
                    'lower': int(rule_range_lower),
                    'upper': int(rule_range_upper)
                },
                'char':char,
                'password':password
            })

    # now, loop thru list and check which passwords are valid
    num_valid = 0
    for pass_data in passwords:
        # setup vars
        char = pass_data['char']
        password = pass_data['password']
        lower_range = pass_data['range']['lower']
        upper_range = pass_data['range']['upper']
        # get count of char in password
        num_occur = password.count(char)
        if lower_range <= num_occur <= upper_range:
            num_valid+=1
    print(f'{num_valid} passwords are valid.')

if __name__ == "__main__":
    main()