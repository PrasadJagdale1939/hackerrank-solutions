# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:12 a.m.
# Technique   basic-arithmetic-operations
# Time        O(1)
# Space       O(1)
# Insight     The program performs standard arithmetic operations on two input integers and prints the results sequentially as required by the problem statement.
# Interview   Before: "How do I handle multiple arithmetic outputs?" After: "You simply perform the operations and print each result on a new line. This approach runs in O(1) time and O(1) space, correctly handling the two input integers provided via standard input."
# Pitfalls    (1) Failing to convert input strings to integers using int() before performing arithmetic operations.  (2) Printing the results in the incorrect order specified by the problem statement.  (3) Omitting the required newline separation between the sum, difference, and product.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
