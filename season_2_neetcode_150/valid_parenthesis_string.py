"""

https://leetcode.com/problems/valid-parenthesis-string/

- contains (, ), *
- valid paren
- * is single paren or empty string

ideas:
- traditional algorithm, but on hit *, first assume "". Then go forward and find first paren where it breaks. If extra ), need (. if missing, need ).
- correctness?

"""

