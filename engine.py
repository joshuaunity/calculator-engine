class CalEngine:
    # def __init__(self, tokens):
    #     self.tokens = tokens


    def process_tokens(self, tokens):
        # result = tokens.find()
        pass
    

    def clean_input(self, tokens):
        tokens = tokens.lower().replace(" ", "")
        letters = "abcdefghijklmnopqrstuvwxyz"
        for e in tokens:
            if e in letters:
                # raise error
                return {"error": "Invalid Input"}
        return tokens
    

    def convert_tokens(self, tokens, operator, d_type=float):
        # split tokens into a list
        tokens = tokens.split(tokens, operator)
        # convert the values from string to floats
        values = [d_type(i) for i in tokens]
        return values


    def process_brackets(self, tokens):
        indexes = []
        for e in tokens:
            if e == "(" or e == ")":
                indexes.append(self, tokens.index(e))
        

    def addition(self, tokens):
        # split tokens into a list and convert to floats
        values = self.convert_tokens(tokens, "+")
        total = sum(values)
        return total


    def multiplication(self, tokens):
        # split tokens into a list and convert to floats
        values = self.convert_tokens(tokens, "*")
        total


    def division(self, tokens):
        pass


    def subtraction(self, tokens):
        pass




# BODMAS

# B - Brackets - ()
# O - Orders - Exponents - 2^3
# D - Division - 2/3
# M - Multiplication - 2*3
# A - Addition - 2+3
# S - Subtraction - 2-3

cal_engine = CalEngine()
print(CalEngine.clean_input("jfndof()jfe(k fmsko23()"))