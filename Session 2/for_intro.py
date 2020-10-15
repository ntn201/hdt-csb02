# print("Hello")
# print("Hello")
# print("Hello")

# iterative
# range(stop)
# range(start, stop)
# range(start, stop, step)
# for i in range(3, 20):
#     print(i)


# In ra tất cả các số tự nhiên chia hết cho 3 và nhỏ hơn 50
# for i in range(50):
#     if i%3 == 0:
#         print(i)

# for i in range(0, 50, 3):
#     print(i)

# Nhập vào 1 số N
# a.) Tính tổng các số từ 1 đến N
# b.) Tính N giai thừa
# c.) Tính số fibbonacci thứ N
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1,n+1):
#     total = total + i
# print(total)

n = int(input("Enter a number: "))
prev = 1
curr = 1
for i in range(2,n+1):
    temp = curr
    curr = prev + curr
    prev = temp
    # print(prev, curr)
print(curr)

