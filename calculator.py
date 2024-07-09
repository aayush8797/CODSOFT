#Simple Calculator

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def power(n1,n2):
    return n1**n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : power
}

num_1 = float(input("what's your first number? : "))
operation_symbol = input("Pick an operation: ")
num_2 = float(input("What's your next number? : "))
calculation = operations[operation_symbol]
answer = calculation(num_1,num_2)
print(f" {num_1} {operation_symbol} {num_2} = {answer}") 
