number = int(input("Your Number : "))
for x in range(number):
    text = " "
    print(text * (number-x) + "*" * (2*x+1))