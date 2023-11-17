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
        # convert tokens to a list
        tokens = list(tokens)
        # loop through the tokens and convert any numbers to float
        for token in tokens:
            if token.isdigit():
                tokens[tokens.index(token)] = float(token)
        return tokens

    @classmethod
    def clear_operator_tokens(self, tokens, operator, d_type=float):
        new_cleaned_list = []
        for e in tokens:
            if e != operator:
                new_cleaned_list.append(e)
        print("new_cleaned_list", new_cleaned_list)
        return new_cleaned_list

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
            print("result_one", result)
            return result

        return "done"

        # get starting inner brackets
        start = (len(indexes) / 2) - 1
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
    def edge_detection(self, tokens, operator_index, result):
        # get token before operators left value
        tokens_before_operator = tokens[:operator_index]
        # get token after operators right value
        tokens_after_operator = tokens[operator_index + 1 :]
        print("tokens_before_operator", tokens_before_operator)
        print("tokens_after_operator", tokens_after_operator)
        print("tokens_@_edge_detection", tokens)
        print("result-two", result)
        print("====================================")
        # check if either of the values on the sode are the only values in the equation
        if len(tokens_before_operator) <= 1 and len(tokens_after_operator) > 1:
            # update the token_after variable as slicing works differently on the right side
            new_tokens_after_operator = tokens[operator_index + 2 :]
            # concatenate the tokens with the result in the middle
            new_tokens = f"{result}{new_tokens_after_operator}"
            print("new_tokens_i", new_tokens)
            return self.calculate_equation(new_tokens)
        elif len(tokens_after_operator) <= 1 and len(tokens_before_operator) > 1:
            # concatenate the tokens with the result in the middle
            new_tokens = f"{tokens_before_operator}{result}"
            print("new_tokens_ii", new_tokens)
            return self.calculate_equation(new_tokens)
        elif len(tokens_after_operator) > 1 and len(tokens_before_operator) > 1:
            # update the token_after variable as slicing works differently on the right side
            new_tokens_after_operator = tokens[operator_index + 2 :]
            # concatenate the tokens with the result in the middle
            new_tokens = f"{tokens_before_operator}{result}{new_tokens_after_operator}"
            print("new_tokens_iii", new_tokens)
            return self.calculate_equation(new_tokens)
        else:
            return result

    @classmethod
    def operator_detection(self, tokens, operator):
        # get operator sign index
        operator_index = tokens.index(operator)
        print("operator_index-operator_detection", operator_index)

        # fetch tokens before and after the operator
        associated_tokens = [tokens[operator_index-1], operator, tokens[operator_index+1]]
        print("====================================")
        print("tokens", tokens)
        print("associated_tokens", associated_tokens)
        result = self.addition(associated_tokens)
        # print("operator_part_result", result)
        print("====================================")

        # detect edges
        return self.edge_detection(tokens, operator_index, result)

    @classmethod
    def calculate_equation(self, tokens):
        if "+" in tokens:
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
        # clean list of all operators
        values = self.clear_operator_tokens(tokens, "+")
        print("values---", values)
        total = sum(values)
        return round(total, 2)

    @classmethod
    def multiplication(self, tokens):
        # split tokens into a list and convert to floats
        values = self.clear_operator_tokens(tokens, "*")
        total = values[0]
        for i in values[1:]:
            total *= i
        return total

    @classmethod
    def division(self, tokens):
        # split tokens into a list and convert to floats
        values = self.clear_operator_tokens(tokens, "/")
        total = values[0]
        for i in values[1:]:
            total /= i
        return total

    @classmethod
    def subtraction(self, tokens):
        # split tokens into a list and convert to floats
        values = self.clear_operator_tokens(tokens, "-")
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
cleaned_tokens = CalEngine.clean_input("3+4+1")
solve_brackets = CalEngine.process_brackets(cleaned_tokens)
print(solve_brackets)
