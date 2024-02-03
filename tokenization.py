# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

import re

class Tokenization:
    def tokenize(exp):
        # Operators to be considered as separate tokens
        operators = ['+', '-', '*', '/', '**']

        tokens = []
        current_token = ''

        is_unary_minus = True # Flag to track unary minus

        for char in exp:

            # Skip whitespace characters
            if char.isspace():
                continue
            
            # alnum returns "true" is the char is a letter or a number
            if char.isalnum() or char == '.':
                current_token += char # char is appended into current_token variable
                is_unary_minus = False  # Reset the unary_minus flag 
            
            elif char == '-' and is_unary_minus:
                # Handle unary minus
                current_token += char
                is_unary_minus = False

            elif char in operators:
                # Handle operators
                if current_token:
                    tokens.append(current_token)
                    current_token = ''

                if tokens and tokens[-1] == char:
                    # Combine consecutive asterisks
                    tokens[-1] = '**'
                else:
                    tokens.append(char)

                is_unary_minus = True  # Reset the unary_minus flag

            elif char == '(':
                # Handle opening parenthesis
                if current_token:
                    tokens.append(current_token)
                    current_token = ''

                tokens.append(char)
                is_unary_minus = True  # Reset the unary_minus flag

            elif char == ')':
                # Handle closing parenthesis
                if current_token:
                    tokens.append(current_token)
                    current_token = ''

                tokens.append(char)

            else:
                # Raise an error for invalid characters
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

# Example usage:
# expression = "( -1 ** 9) + - 3)"
# tokens = Tokenization.tokenize(expression) # handle the scenario where 2 operators like +- are back to back
# print(tokens)


# reg_expression = "(432*(34.35-23/235) - 392 / 31)"
# # Using regex-based tokenization
# regex_tokens = Tokenization.tokenize_with_regex(reg_expression)
# print(regex_tokens)

