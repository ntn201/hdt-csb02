pascal = [[1], [1, 1]]

n = int(input("enter a number: "))

if n <= 0: 
    print("Please enter positive number")

elif n == 1:
    print(pascal[0][0])

elif n == 2:
    for i in pascal:
        print(i)

else:

    for i in range(n-2):
        temp_arr = [1]
        for number in range(len(pascal[-1])-1):
            newNumber = pascal[-1][number] + pascal[-1][number+1]
            temp_arr.append(newNumber)
        temp_arr.append(1)
    
        pascal.append(temp_arr)

    for arr in pascal:
        print(arr)
    
            