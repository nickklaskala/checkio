#!/usr/bin/env checkio --domain=py run reverse-engineer

# You are standing next to a math machine which takes two numerical inputsxandy,    and has a single numerical output.    It is known that the machine evaluates an expression usingx,y,    the operators+ – * /andbrackets.    You should recover the expression by using the machine and the inputs of your choice over several turns.x,yand the result you receive are integers.    The machine uses real division(/) in the expression.    When dividing by zero, the result will evaluate to"ZeroDivisionError".
# 
# Equivalent expressions will be accepted by the grader.    For this the machine evaluates your expression and the hidden expression several times using random values.
# 
# In each step your function gets a list with data from the past steps.    Each element is a list of three numbers --x(int),y(int) andoutput(a fraction as a list or the string "ZeroDivisionError").    The output is represented as a list with two integers - numerator and denominator.
# 
# The function should return a list with three elements --    your guess as an expression string,xandy, as integers.
# 
# Input:A list with data from the past steps.
# 
# Output:A list with three elements -- your guess as an expression string,x(int) andy(int).
# 
# Precondition:The hidden expression is correct. It does not evaluate at ZeroDivisionError always.
# 
# 
# 
# END_DESC

def checkio(steps):
    return ["x+y", 1, -1]

#This part is using only for self-testing
#It's "light" version of the grader
#The hidden expression should be correct (non x/(y-y))
if __name__ == '__main__':
    def test_it(hidden_expression, solver):
        from fractions import Fraction
        from random import randint

        def check_is_right(guess, expression):
            for _ in range(10):
                result_guess = 0
                result_expr = 1
                for __ in range(100):
                    x, y = Fraction(randint(-100, 100)), Fraction(randint(-100, 100))
                    try:
                        result_expr = eval(expression)
                        result_guess = eval(guess)
                    except ZeroDivisionError:
                        continue
                    break
                if result_guess != result_expr:
                    return False
            return True
    
        input_data = []
        for step in range(50):
            user_guess, x_real, y_real = solver(input_data)
            x = Fraction(x_real)
            y = Fraction(y_real)
            try:
                result = eval(hidden_expression)
                output = [result.numerator, result.denominator]
            except ZeroDivisionError:
                output = "ZeroDivisionError"
            input_data.append([x_real, y_real, output])
            if check_is_right(user_guess, hidden_expression):
                return True
        else:
            return False

    assert test_it("x+y", checkio), "x+y"
    assert test_it("x*y", checkio), "x*y"
    assert test_it("x-y", checkio), "x-y"
    assert test_it("x/y", checkio), "x/y"