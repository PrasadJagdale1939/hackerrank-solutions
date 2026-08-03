# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
# Problem     Python: Division
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:17 a.m.
# Technique   arithmetic-division-operators
# Time        O(1)
# Space       O(1)
# Insight     The implementation utilizes Python's floor division operator to compute the integer quotient and the standard division operator to compute the floating-point quotient.
# Interview   Before: "How do I perform division in Python?" After: "Python provides the // operator for floor division and the / operator for float division, both executing in O(1) time. Note that division by zero will raise a ZeroDivisionError if the second input is zero."
# Pitfalls    (1) Confusing the floor division operator // with the standard division operator /.  (2) Failing to account for the ZeroDivisionError when the second input is zero.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)
