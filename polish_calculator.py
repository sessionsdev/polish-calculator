# Recursive decent parser

class PolishCalculator:

    def __init__(self):
        pass


    def validate_terms(self, expression):
        stack = []
        for i in expression:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) < 1:
                    raise SyntaxError("Unexpected ')'")
                else:
                    stack.pop()
        if len(stack) >= 1:
            raise SyntaxError("Expected ')'.  Did not get.")



    def parse_exp(self, str):
        self.validate_terms(str)
        stack = []
        terms = list(str)
        term = []
        for i in terms:
            stack.append(i)
            if i == ")":
                while 



class Expression:

    def __init__(self, terms):
        self.terms = terms
        self.token_map = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            # "sqrt": lambda x: x**(1/2)
        }


    def evaluate(self):
        operator = self.token_map.get(self.terms[0])
        result = operator(self.terms[1], self.terms[2])
        return result






            
