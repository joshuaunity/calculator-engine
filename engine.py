class CalEngine(object):
    # def __init__(self, tokens):
    #     self.tokens = tokens


    def process_tokens(self, tokens):
        # result = tokens.find()
        pass
    
    @staticmethod
    def clean_input(tokens):
        tokens = tokens.lower().replace(" ", "")
        letters = "abcdefghijklmnopqrstuvwxyz"
        for e in tokens:
            if e in letters:
                # raise error
                return {"error": "Invalid Input"}
        return tokens
    
    @classmethod
    def convert_tokens(self, tokens, operator, d_type=float):
        # split tokens into a list
        tokens = tokens.split(operator)
        # convert the values from string to floats
        values = [d_type(i) for i in tokens]
        return values

    @classmethod
    def process_brackets(self, tokens):
        indexes = []
        for e in tokens:
            if e == "(" or e == ")":
                indexes.append(tokens.index(e))
        
        if len(indexes) % 2 != 0:
            # raise error
            return {"error": "Invalid Input, Incomplete Brackets"}
        
        # check there are no brackets in the whole equation
        if len(indexes) == 0:
            result = self.calculate_equation(tokens)
            print("result", result)
            return result
        
        return "done"
        
        # get starting inner brackets
        start = (len(indexes)/2) - 1
        # get ending inner brackets
        end = start + 1
        bracket_tokens = tokens[start:end]
        # calculate the equation in the brackets
        result = self.calculate_equation(bracket_tokens)
        # replace the brackets with the result
        tokens[start:end] = result
        # recursively call the function
        return self.process_brackets(tokens)

    @classmethod
    def edge_detection(self, tokens, operator, operator_index, result):
        # check if either of the tokens before or after the operator are at the end of the equation
        if tokens.index(tokens[operator_index-1]) <= 0 or tokens.index(tokens[operator_index+1]) >= len(tokens):
            # get token before operators left value
            tokens_before_operator = tokens[:operator_index]
            # get token after operators right value
            tokens_after_operator = tokens[operator_index+1:]
            # concatenate the tokens with the result in the middle
            new_tokens = f"{tokens_before_operator}{result}{tokens_after_operator}"
            print("before", tokens.index(tokens[:operator_index]))
            print("new_tokens", new_tokens)
            print("tokens", tokens)
            print("tokens_before_operator", tokens_before_operator)
            print("tokens_after_operator", tokens_after_operator)
            return "done"
            return self.calculate_equation(new_tokens)
        elif tokens.index(tokens[:operator_index]) == 0:
            # get token after operators right value
            tokens_after_operator = tokens[operator_index+1:]
            # concatenate the tokens with the result in the middle
            new_tokens = f"{result}{tokens_after_operator}"
            return self.calculate_equation(new_tokens)
        elif tokens.index(tokens[operator_index+1:]) == len(tokens):
            # get token before operators left value
            tokens_before_operator = tokens[:operator_index]
            # concatenate the tokens with the result in the middle
            new_tokens = f"{tokens_before_operator}{result}"
            return self.calculate_equation(new_tokens)
        else:
            new_tokens = result

        # check if there are any more plus(+) operators
            if operator in new_tokens:
                # recursively call the function
                return self.calculate_equation(new_tokens)
            else:
                return new_tokens

    @classmethod
    def operator_detection(self, tokens, operator):
        # get operator sign index
        operator_index = tokens.index(operator)
        # fetch tokens before and after the operator
        associated_tokens = f"{tokens[operator_index-1]}{operator}{tokens[operator_index+1]}"
        result = self.addition(associated_tokens)
        # detect edges
        self.edge_detection(tokens, operator, operator_index, result)


    @classmethod
    def calculate_equation(self, tokens):
        if "+" in tokens:
            print("additon detected", tokens)
            return self.operator_detection(tokens, operator="+")
        # elif "-" in tokens:
        #     print("subtraction detected", tokens)
        #     return self.operator_detection(tokens, operator="-")
        # elif "*" in tokens:
        #     print("multiplication detected", tokens)
        #     return self.operator_detection(tokens, operator="*")
        # elif "/" in tokens:
        #     print("division detected", tokens)
        #     return self.operator_detection(tokens, operator="/")
        else:
            return tokens
            

    @classmethod
    def addition(self, tokens):
        # split tokens into a list and convert to floats
        values = self.convert_tokens(tokens, "+")
        # print("values", values)
        total = sum(values)
        print("values", values)
        print("total", total)
        return total

    @classmethod
    def multiplication(self, tokens):
        # split tokens into a list and convert to floats
        values = self.convert_tokens(tokens, "*")
        total = values[0]
        for i in values[1:]:
            total *= i
        return total

    @classmethod
    def division(self, tokens):
        # split tokens into a list and convert to floats
        values = self.convert_tokens(tokens, "/")
        total = values[0]
        for i in values[1:]:
            total /= i
        return total

    @classmethod
    def subtraction(self, tokens):
        # split tokens into a list and convert to floats
        values = self.convert_tokens(tokens, "-")
        total = values[0]
        for i in values[1:]:
            total -= i
        return total




# BODMAS

# B - Brackets - ()
# O - Orders - Exponents - 2^3
# D - Division - 2/3
# M - Multiplication - 2*3
# A - Addition - 2+3
# S - Subtraction - 2-3

cal_engine = CalEngine()
cleaned_tokens = CalEngine.clean_input("3+4")
solve_brackets = CalEngine.process_brackets(cleaned_tokens)
print(solve_brackets)