class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operant_2 = stack.pop()
                operant_1 = stack.pop()
                if token == "+":
                    result = operant_1 + operant_2
                elif token == "-":
                    result = operant_1 - operant_2
                elif token == "*":
                    result = operant_1 * operant_2
                else:
                    result = int(float(operant_1) / float(operant_2))
                stack.append(result)

        return stack[0]


