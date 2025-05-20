"""
Solutions to module 2 - A calculator
Student: Alva Christensson
Mail: alvachristensson03@gmail.com
Reviewed by: Divya
Reviewed date: 2024-0923
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def log(n):
    if(n>0):
        return math.log(n)
    
    else:
        raise EvaluationError(f"Argument to ln is {n}. Argument must be an integer > 0")

def cos(v):
    try:
        return math.cos(v)
    
    except :
        raise EvaluationError(f"Argument to cos is {v}. Argument must be an number or variable")

def sin(v):
    try:
        return math.sin(v)
    
    except:
        raise EvaluationError(f"Argument to sin is {v}. Argument must be an number or variable")

def exp(x):
    try:
        return math.exp(x)
    
    except :
        raise EvaluationError(f"Argument to sin is {x}. Argument must be an number or variabel")

def fib(n):
    memory = {0:0, 1:1}

    def fib_mem(n):
        if n not in memory:
            memory[n] = fib_mem(n-1) + fib_mem(n-2)
        return memory[n]
    
    if(int(n)):
        return int(fib_mem(n))
    
    else:
        raise EvaluationError(f"Argument to fib is {n}. Argument must be an integer >= 0")

def fac(n):
    if(n >= 0 and int(n)):
        if n == 1:
            return 1
        else:
            n = int(n)
            return n *fac(n-1)
        
    else:
        raise EvaluationError(f"Argument to fac is {n}. Argument must be an integer >= 0")
        



def arglist(wtok, variables):
    args = []
    if wtok.get_current() == '(':
        wtok.next()  

        while wtok.get_current() != ')':
            args.append(assignment(wtok, variables))

            if wtok.get_current() == ',':
                wtok.next()  

            elif wtok.get_current() != ')':
                raise SyntaxError("Expected ',' or ')' in argument list")

        wtok.next()
    else:
        raise SyntaxError("Expected '(' at start of argument list")

    return args  
        


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end() == False:
        raise SyntaxError("Expected EOL")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    #For multiple assignments it must be a while loop not an if.
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[str(wtok.get_current())] = result
        else:
            raise SyntaxError("Excpected variable after '='")
        wtok.next()

    return result

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':        
        if(wtok.get_current() == '+'):
            wtok.next()
            result = result + term(wtok, variables)
        
        elif (wtok.get_current() == '-'):
            wtok.next()
            result = result - term(wtok, variables)

    if wtok.is_number():
        raise SyntaxError("Expected operator")

    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/': 
        if(wtok.get_current() == '*'):
            wtok.next()
            result = result * factor(wtok, variables)
        
        elif (wtok.get_current() == '/'):
            wtok.next()
            fac = factor(wtok, variables)
            if fac == 0:
                raise EvaluationError("Division by zero")
            
            result = result / fac
        



    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1Dict = {"log":log,
                      "cos":cos,
                      "sin":sin,
                      "exp":exp,
                      "fac":fac,
                      "fib":fib,}
    
    function_nDict = {"max":max,
                      "sum":sum,}
    

    
    if wtok.get_current() == '(':
        wtok.next() 
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    
    elif wtok.get_current() in function_1Dict:
        func = wtok.get_current()
        wtok.next()

        if wtok.get_current() == '(':
            wtok.next()
            res = assignment(wtok,variables)

            result = function_1Dict[func](res)
            wtok.next()

        else:
            raise SyntaxError("Expected '(' after function name")
        
    elif wtok.get_current() in function_nDict:
        func = wtok.get_current()
        wtok.next()
        
        res = arglist(wtok,variables)

        result = function_nDict[func](res)
        wtok.next()

            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.is_name():
        try:
            result = variables[wtok.get_current()]
            wtok.next()

        except:
            raise EvaluationError(f"Undefined variable: '{wtok.get_current()}'")


    elif wtok.get_current() == '-':
        wtok.next()  
        result = -factor(wtok, variables)

    else:
        raise SyntaxError("Expected number or '('")  
    return result


         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"E": math.e, "PI": math.pi, "ans": 0.0}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = r'C:\Users\alvac\OneDrive\Skrivbord\Universitet\Programmering 2\Inlämningsuppgifter\MA2\MA2Files\MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()

    except FileNotFoundError:
        pass
    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()

        elif wtok.get_current() == "vars":
            for var_name, value in variables.items():
                print(f"{var_name}: {value:}")

        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except EvaluationError as ee:
                print("*** Evalution error", ee)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()
