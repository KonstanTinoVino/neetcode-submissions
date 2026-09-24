from typing import List
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "%": operator.mod,
            "^": operator.xor,
            "/": operator.truediv
        }

        for element in tokens:
            if element.lstrip("-").isdigit():
                stack.append(int(element))
            else:
                element1 = stack.pop()
                element2 = stack.pop()
                stack.append(int(ops[element](element2, element1)))
        return stack.pop()