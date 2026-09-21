"""
Create helper functions for add, subtract, multiply, divide
Create dict that corresponds operators to functions
Create a first and second variable and store first two values in them
iterate through the rest of the values, applying the operator and then storing the result in one and the second number in the other
"""

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return int(a / b)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if not tokens:
            return 0

        funcs = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
        }

        stack = []

        for tok in tokens:

            try:
                stack.append(int(tok))
            except ValueError:
                if tok in funcs:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(funcs[tok](first, second))
                else:
                    return -1
        
        return stack[-1]



