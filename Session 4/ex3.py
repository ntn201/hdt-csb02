string1 = input('enter smth: ')

newString = ''

for i in range(len(string1)-1, -1, -1):
    newString += string1[i]

if newString == string1:
    print("This is palidrome")

else:
    print('not palidrome')