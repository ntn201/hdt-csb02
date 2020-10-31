A = [4, 2, 5, 10, 9]
B = []
while len(A):
    smallest = A[0]

    for number in A:
        if smallest > number:
            smallest = number
    
    B.append(smallest)
    A.remove(smallest)

print(B)
print(A)

