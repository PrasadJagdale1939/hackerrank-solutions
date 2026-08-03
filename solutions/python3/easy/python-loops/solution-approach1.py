# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
# Problem     Loops
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:30 a.m.
# Technique   range-based-iteration
# Time        O(n)
# Space       O(1)
# Insight     The loop iterates through all non-negative integers i strictly less than n, calculating and printing the square of each value.
# Interview   Before: "How would you print the squares of all integers from 0 up to n-1?" After: "I used a range(n) loop to iterate n times, which achieves O(n) time complexity and O(1) space, correctly handling the constraint i < n."
# Pitfalls    (1) Using range(n + 1) instead of range(n) would include the square of n, violating the i < n constraint.  (2) Failing to convert the input string to an integer using int() will cause a TypeError during the multiplication operation.
# ──────────────────────────────────────────────────

n = int(input())
for i in range(n):
    print(i * i)

