class Interpreter:
    def __init__(self):
        self.symbolTable = {}

    def eval(self, expression):
        tokens = expression.split()

        if not tokens:
            return "Error! Empty Input"

        if tokens[0] == "if":
            return self.evalIfElse(tokens)

        if tokens[0] == "while":
            return self.evalWhileLoop(tokens)
        
        if "=" in tokens:
            if tokens.count("=") > 1: 
                return "Syntax Error: Invalid Assignment"
            
            var_name = tokens[0]
            if not var_name.isalpha():
                return f"Semantic Error: Invalid variable name '{var_name}'"
            try:
                value = self.evalExpression(tokens[2:])
                self.symbolTable[var_name] = value
                return value  
            except:
                return "Syntax Error: Invalid Assignment"

        try:
            return self.evalExpression(tokens)
        except:
            return "Syntax Error: Unexpected Token"

    def evalIfElse(self, tokens):
        try:
            if "then" not in tokens or "else" not in tokens:
                return "Syntax Error: Invalid if-else statement"

            then_index = tokens.index("then")
            else_index = tokens.index("else")

            condition_tokens = tokens[1:then_index]  
            true_tokens = tokens[then_index + 1:else_index]  
            false_tokens = tokens[else_index + 1:] 

            condition_result = self.evalExpression(condition_tokens)

            chosen_tokens = true_tokens if condition_result else false_tokens

            if len(chosen_tokens) < 3 or chosen_tokens[1] != "=":
                return "Syntax Error: Invalid if-else assignment"

            var_name = chosen_tokens[0]
            value = self.evalExpression(chosen_tokens[2:])
            self.symbolTable[var_name] = value
            return value  

        except:
            return "Syntax Error: Invalid if-else statement"

    def evalWhileLoop(self, tokens):
        try:
            if "do" not in tokens:
                return "Syntax Error: Invalid while loop"
            
            condition_index = tokens.index("while") + 1
            do_index = tokens.index("do")
            
            condition_tokens = tokens[condition_index:do_index]  
            loop_body_tokens = tokens[do_index + 1:]  
            
            while True:
                condition_result = self.evalExpression(condition_tokens)
                if not condition_result: 
                    break

                result = self.eval(" ".join(loop_body_tokens))
                if result != "Syntax Error":  
                    continue
                else:  
                    break

            return f"Loop executed successfully."
        
        except:
            return "Syntax Error: Invalid while loop"

    def evalExpression(self, tokens):
        expr = " ".join(tokens)

        for var in self.symbolTable:
            expr = expr.replace(var, str(self.symbolTable[var]))

        expr = expr.replace("^", "**")  

        try:
            return eval(expr)
        except:
            return "Syntax Error"

interpret = Interpreter()
while True:
    Input = input("~ ")
    if Input.lower() == "exit":
        break

    result = interpret.eval(Input)
    if result is not None:
        print(f"Result: {result}")






