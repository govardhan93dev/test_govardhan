n1 = int(input("Enter number 1: ")) 
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))

total = []
total.append(n1)  # here we are appending the input values
total.append(n2)
total.append(n3)
total.append(n4)
total.append(n5)

x = sorted(total)  # here user inputs can be sorted
print(x)  