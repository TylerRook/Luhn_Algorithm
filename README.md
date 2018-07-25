# Luhn_Algorithm
This is an implementation of the Luhn Algorithm used for various forms of ID validation. 

## Algorithm steps, given an ID number:
1. Double the value of every second digit starting from the right.
2. Sum all the digits.
3. Calculate the remainder when the sum is divided by 10.
4. If the remainder equals 0, the identification number is valid.

## Input Format:
4012888888881881

## Output Format:
Credit Card 4012888888881881 is valid.

-OR-

Credit Card 4012888888881882 is not valid.
