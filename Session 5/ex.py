def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_digit(n):
    total = 0
    while n > 0:
        total += n%10
        n = n // 10
    return total

n = int(input("Enter a number: "))
print(is_prime(n))
print(n%sum_digit(n)==0)

