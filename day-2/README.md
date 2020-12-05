
## Day 2: Password Philosophy

Part One
--
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?


Part Two
--
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?


Explanations
--

### Part one:
This'n here was pretty simple; looped thru the list of passwords/rulesets, and created a dictionary for each containing the range, char to be checked for, and the password itself.
I then looped through the list of dictionaries and checked to see if each password matched the ruleset, and added to a var if it did.
After all passwords had been checked, print the total num_valid to console.

### Part two:
I'll be honest -- I read the question wrong like 4 separate times.
This one uses the same data, so I copy+pasted code from part one. However, rather than looking for a number of occurences, this looked for char to be at the two indexes provided (non-zero indexes). The part I misread is that this problem calls for an **XOR** operator, **not** an **OR**. So the character must occur at **one and only one** of the given positions.
This used the same logic/process as part one. Loop thru all passwords, checked if each matched the ruleset, then print total num_valid to the console.