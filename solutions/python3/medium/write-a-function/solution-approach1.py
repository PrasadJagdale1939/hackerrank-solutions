# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-03, 10:57 a.m.
# Technique   boolean-logic-conditional
# Time        O(1)
# Space       O(1)
# Insight     The function evaluates the Gregorian leap year criteria by combining divisibility rules into a single boolean expression that returns true if the year is divisible by 400 or (divisible by 4 and not by 100).
# Interview   Before: "How would you determine if a year is a leap year?" After: "I implemented the Gregorian calendar logic using O(1) time and space complexity, ensuring that years divisible by 100 are only leap years if they are also divisible by 400."
# Pitfalls    (1) Incorrect operator precedence between logical AND and OR can lead to false positives for century years.  (2) Failing to account for the exception where years divisible by 100 are not leap years unless also divisible by 400.
# ──────────────────────────────────────────────────

def is_leap(year):
    leap = False
    
    if(year%4==0 and year%100!=0 or year%400==0):
        leap = True
    return leap

