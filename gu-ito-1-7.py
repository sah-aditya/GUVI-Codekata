'''Richard Hendricks, Gilfoyle, and Dinesh, the brilliant minds behind Pied Piper, are on a mission to optimize their messaging platform's data compression algorithm. They aim to represent "Yes" and "No" messages more efficiently by converting them into a different base that requires fewer characters, thus reducing the overall message size.

Richard explains that they currently represent "Yes" messages as 1 and "No" messages as 0 in their messaging platform. However, he believes they can further compress this representation by changing the base to a more efficient one, achieving a four-fold decrease in the number of characters needed to represent the messages.

Gilfoyle immediately jumps in, suggesting a strategy to change the base of the representation to achieve their goal. With his expertise in cryptography and data compression, Gilfoyle proposes a solution to map the binary representation onto a different base that requires only one-fourth of the characters needed in the existing base.

Help Gilfoyle defend his case and determine the optimal base for representing "Yes" and "No" messages to achieve a four-fold decrease in the number of characters required.

Input:

A single line containing a string made up of 0's and 1's representing "Yes" and "No" messages.
Input Constraints: 1 ≤ N ≤ 57, where N is the number of characters (0's and 1's) in the string.

Output:

Single line denoting the value of the binary string in a base that uses four times fewer characters than the existing base.

Sample input:

10110111000010010011011001010111111000111010010010000

Sample output:

16e126cafc7490'''


a = input()

def base(b):
    basesn=hex(int(b,2))[2:]
    return basesn

print(base(a))
    


