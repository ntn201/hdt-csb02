# menu = ["Com", "Pho", "Banh gio", "Banh cuon"]
#         #   0      1         2           3
# # print(menu)
# menu[0] = "Banh xeo"
# # print(menu)

# menu.append("Banh da")
# menu.insert(2,"Bun")
# # print(menu)

# menu.remove("Pho")
# menu.pop(3)
# # menu.remove(2)
# print(menu)


# Tao 1 list chua 3 so thich cua em
# Cho nguoi dung nhap vao mot so thich moi va in ra list sau khi da thay doi

# append(value): thêm một phân tử vào cuối list
# insert(index,value): thêm phần tử vào vị trí bất kì
# remove(value): xóa phần tử có giá trị value
# pop(): xóa phần tử cuối cùng
# pop(index): xóa phần tử thứ index


# Nhập vào một số n. Sau đó cho người dùng nhập vào n chữ số.
# In ra những chữ số đã nhập vào

# Tính tổng các chữ số đã nhập vào.

# n = int(input("Enter n: "))
# arr = []
# for i in range(n):
#     number = int(input("Enter a number: "))
#     arr.append(number)
# print(arr)

# total = 0
# for i in arr:
#     # print(i)
#     total = total + i
# print(total)

# for i in range(len(menu)):
#     print(menu[i])


# Nhập vào n, in ra số fibbonacci thứ n.
fib = [1,1]
n = int(input("Enter n: "))
for i in range(n-1):
    prev = fib[len(fib)-2]
    curr = fib[len(fib)-1]
    fib.append(prev + curr)
print(fib[n])
print(fib)

# Nhập vào số N, in ra N tầng đầu tiên của tam giác pascal+-  