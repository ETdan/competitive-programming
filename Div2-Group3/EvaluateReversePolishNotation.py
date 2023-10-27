class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) <= 1:
            return int(tokens[0])

        container = []
        operators = ["*", "/", "+", "-"]
        for val in tokens:
            if val not in operators:
                container.append(val)
            else:
                second = int(container[-1])
                first = int(container[-2])

                container = container[:-2]

                if val == "+":
                    container.append(first + second)
                if val == "-":
                    container.append(first - second)
                if val == "*":
                    container.append(first * second)
                if val == "/":
                    r = first / second
                    r = -(abs(first) / abs(second)) if r < 0 else r
                    container.append(r)

        #     print(container)
        # print(-6 / 132)
        return container[0]
        
