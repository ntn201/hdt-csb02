# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# delta = b*b - 4*a*c
# print(delta)

# if delta > 0:
#     x1 = (-b + delta**0.5) / (2*a)
#     x2 = (-b - delta**0.5) / (2*a) 
#     print("Phuong trinh co 2 nghiem: x1 =", x1, "x2 =", x2)

# if delta == 0:
#     x = -b / (2*a)
#     print("Phuong trinh co nghiem kep: x =", x)

# if delta < 0:
#     print("Phuong trinh vo nghiem") 



age = int(input("How old are you: "))

if age < 3:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")