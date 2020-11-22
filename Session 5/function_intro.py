# n = 20

# # Define a function
# def is_prime(n): #n : parameter
#     prime = True
#     for i in range(2,n):
#         if n % i == 0:
#             prime = False
#     print(prime)


# # Call a function
# is_prime(50)
# is_prime(73)
# is_prime(113)


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# delta = b**2 - 4*a*c

# if delta > 0:
#     x1 = (-b+delta**0.5)/(2*a)
#     x2 = (-b-delta**0.5)/(2*a)
#     print(x1,x2)
# if delta = 0:
#     x = (-b)/(2*a)
#     print(x)
# if delta < 0:
#     print("No solution!")

# def function_name(parameters):
#     code
#     return

def calculate_delta(a,b,c):
    delta = b**2 - 4*a*c
    return delta

def calculate_x(a,b,delta):
    if delta > 0:
        x1 = (-b+delta**0.5)/(2*a)
        x2 = (-b-delta**0.5)/(2*a)
        return x1, x2
    if delta == 0:
        x = -b/(2*a)
        return x
    if delta < 0:
        return None

def solve_quadratic(a,b,c):
    delta = calculate_delta(a,b,c)
    x = calculate_x(a,b,delta)
    return x

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
a = 1
b = 2
c = -3

x = solve_quadratic(a,b,c)

print(x)

# ...
# .
# .
# .
# .
# .

# prime = True
# for i in range(2,n):
#     if n % i == 0:
#         prime = False
# print(prime)




# .
# .
# .
# .
# .
# .

# prime = True
# for i in range(2,n):
#     if n % i == 0:
#         prime = False
# print(prime)