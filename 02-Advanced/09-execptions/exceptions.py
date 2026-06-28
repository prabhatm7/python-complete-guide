# SyntaxError 
a = 5 
#print(5)) # SyntaxError: unmatched ')'

# TypeError
# a = 5 + '10'
# print(a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ModuleNotFoundError
# import somemodule  # ModuleNotFoundError: No module named 'somemodule'

# NameError
# print(c) # NameError: name 'c' is not defined

# FileNotFoundError
# f = open("somefile.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'



a = [1, 2, 3]

# IndexError
# print(a[5]) # IndexError: list index out of range

# ValueError
a.append(4)
# a.remove(5) # ValueError: list.remove(x): x not in list

a = {"name": "Alice", "age": 30}
# KeyError
# print(a["gender"]) # KeyError


# raise an exception
x = 5 
if x < 0:
    raise ValueError("x must be positive") # Exception: x must be positive
    # raise ExceptionType("x must be positive")  # raise a specific exception type with a message 


# assert statement
y = -1
# assert y >= 0, "y must be positive" # AssertionError: y must be positive

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print("Error:", e) # Error: division by zero
except TypeError as e:
    print("Error:", e) # Error: unsupported operand type(s) for +: 'float' and 'str'
else:
    print("No error occurred") # No error occurred
finally:
    print("This block always executes") # This block always executes


# custom exception
class ValueTooHighError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value
        
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high!", x) # raise custom exception
    elif x < 0:
        raise ValueTooLowError("Value is too low!", x) # raise custom exception
    else:
        print("Value is acceptable")

try:
    test_value(90)
    test_value(-10)
except ValueTooHighError as e:
    print("Error:", e) # Error: Value 150 is too high!
except ValueTooLowError as e:
    print("Error:", e) # Error: Value -10 is too low!