# Programm to check complex conditions using logical operatrs
a = 6
b = 4
c = 3
if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c):
    print("conditions met")
else:
    print("conditions not met")
    
# function to check input types using logical operators
def check_types(a, b, c):
    if isinstance(a, str) and isinstance(b, int) and isinstance(c, float):
        return "valid input types"
    else:
        return "invalid input types"

#Test case
print(check_types("Hello", 5, 3.14)) #valid input types
print(check_types("Hello", "5", 3.14)) #invalid input types
print(check_types(123, 5, 3.14)) # invalid iunput types

# Script to demonstrate logical operators with boolean values
x = input("enter the value of x:")
y = input("enter the value of y:")

# convert inputs to boolean
x_bool = bool(x)
y_bool = bool(y)

print("x and y:", x_bool and y_bool)
print("x OR y:", x_bool or y_bool)
print("NOT x:", not x_bool)
print("x XOR y:", (x_bool and not y_bool) or (not x_bool and y_bool))
