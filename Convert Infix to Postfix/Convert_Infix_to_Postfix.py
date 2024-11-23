def precedence(op):
    # Return the precedence of operators
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []  # Stack to hold operators and parentheses
    output = []  # Output list to hold the postfix expression
    
    for char in expression:
        # If the character is an operand, add it to the output
        if char.isalnum():  # Assuming operand is alphanumeric (variables or numbers)
            output.append(char)
        
        # If the character is '(', push it to the stack
        elif char == '(':
            stack.append(char)
        
        # If the character is ')', pop until '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        
        # If the character is an operator, pop operators from the stack with higher or equal precedence
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)
    
    # Pop all the remaining operators from the stack
    while stack:
        output.append(stack.pop())
    
    # Join the list into a string and return it as the postfix expression
    return ''.join(output)

# Test cases
expression1 = "A*(B+C)"
expression2 = "(A+B)*(C-D)"

print(f"Expression: {expression1} → Postfix: {infix_to_postfix(expression1)}")
print(f"Expression: {expression2} → Postfix: {infix_to_postfix(expression2)}")

