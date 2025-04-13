class ExpressionEvaluator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def infix_to_postfix(self, expression: str) -> str:
        stack = []
        postfix = []
        
        for token in expression.split():
            if token.isalnum():  # Operando
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Descartar el '('
            else:  # Operador
                while (stack and stack[-1] != '(' and 
                       self.operators[stack[-1]] >= self.operators[token]):
                    postfix.append(stack.pop())
                stack.append(token)
        
        while stack:
            postfix.append(stack.pop())
            
        return ' '.join(postfix)

# Ejemplo de uso
evaluator = ExpressionEvaluator()
print(evaluator.infix_to_postfix("3 + 4 * 2"))  # Output: 3 4 2 * +