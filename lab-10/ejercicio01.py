def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""

    # Dictionary defining operator precedence
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    output = []  # List to store the final postfix expression
    stack = []   # Stack to temporarily hold operators and parentheses

    # Iterate through each token in the infix expression
    for token in tokens:
        if token.isalnum():  # If the token is an operand (letter or number)
            output.append(token)  # Add it directly to the output

        elif token == '(':  # If the token is a left parenthesis
            stack.append(token)  # Push it onto the stack

        elif token == ')':  # If the token is a right parenthesis
            # Pop from the stack to the output until a left parenthesis is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the left parenthesis '('

        else:
            # If the token is an operator (+, -, *, /)
            # While there is an operator at the top of the stack with greater or equal precedence,
            # and it's not a left parenthesis, pop it to the output
            while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            # Push the current operator onto the stack
            stack.append(token)

    # After processing all tokens, pop any remaining operators from the stack to the output
    while stack:
        output.append(stack.pop())

    return output  # Return the postfix expression

# ➕ Simple addition
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])

# 📊 Operator precedence: multiplication before addition
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])

# 🔗 Parentheses change precedence
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])

# 🧮 More complex expression with two grouped subexpressions
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])

# 🔤 Multiple operators and variables
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])