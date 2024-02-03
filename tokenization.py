# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# class Tokenization:
#     # !!! need to settle
#     def token(exp):
#         tokens = exp.split() # look at the spaces 
    
# # good to create a tokenisation class if want to have no spaces, negative number or floats (pretty complex)
# # can use regular expressions
    
# make sure user doesnt put eg."((num))", "/+", "++"
import re

class Tokenization:
    def tokenize(exp):
        # Operators to be considered as separate tokens
        operators = ['+', '-', '*', '/', '**', '(', ')']

        tokens = []
        current_token = ''

        is_unary_minus = True # for negative numbers

        # removes the spaces in between the exp
        for char in exp:

            # basically to not read the space
            if char.isspace():
                continue
            
            # alnum returns "true" is the char is a letter or a number
            if char.isalnum() or char == '.':
                current_token += char # char is appended into current_token variable
                is_unary_minus = False  # Reset the unary_minus flag (means not part of neg number)
            
            elif char == '-' and is_unary_minus:
                current_token += char  # Unary minus is part of the current_token

            elif char in operators:
                # print(char) # char is the operators 
                if current_token:
                    tokens.append(current_token)
                    # print(current_token, "oop") # append the chars
                    current_token = ''
                if char == '*' and tokens[-1] == '*':
                    tokens[-1] = '**' # combine the ** tgt

                elif tokens and tokens[-1] == char: # if the 2 operators are the consectively the same , NEED TO HANDLE THE SITUATION WHEN THERE IS PEDMAS (((DOUBLE BRACKETS TOGETHER)))
                    print(exp, "EXPRESSION")
                    print(tokens[-2], "TOKEN")
                    print(tokens[-1], "TOKEN[-1]")
                    print(char, "CHAR")

                    raise ValueError(f"Invalid consecutive operators: {char}{char}") # find a way to by pass this without causing an error
                
                # elif len(tokens) >= 2 and tokens[-1] in ('+', '-', '/', '**') and char == '/' or char == '+' or char == '**': # handle the case of / with another operator
                #     raise ValueError(f"Invalid operator sequence: {tokens[-1]}{char}")
                
                else:
                    tokens.append(char) # append the operators
                # print(char, "yellow") 
                    
                is_unary_minus = True  # Reset the unary_minus flag for the next iteration

            else:
                raise ValueError(f"Invalid character: {char}")

        if current_token:
            tokens.append(current_token)

        return tokens
    
    # # not sure if this is what a regex does 
    # def tokenize_with_regex(exp):
    #     # Define regular expressions for numbers, operators, and parentheses
    #     # number_pattern = r'\b\d+(\.\d+)?\b'
    #     number_pattern = r'\b\d+(\.\d+)?\b'
    #     operator_pattern = r'[-+*/^()]'
        
    #     # Combine the patterns into a single pattern
    #     combined_pattern = f'{number_pattern}|{operator_pattern}'

    #     # Find all matches using the regular expression
    #     matches = re.findall(combined_pattern, exp)

    #     # Filter out empty strings from the matches
    #     tokens = [match for match in matches if match]

    #     return tokens

# # Example usage:
# expression = "( -1 ** 9) + - 3)"
# tokens = Tokenization.tokenize(expression) # handle the scenario where 2 operators like +- are back to back
# print(tokens)


# reg_expression = "(432*(34.35-23/235) - 392 / 31)"
# # Using regex-based tokenization
# regex_tokens = Tokenization.tokenize_with_regex(reg_expression)
# print(regex_tokens)