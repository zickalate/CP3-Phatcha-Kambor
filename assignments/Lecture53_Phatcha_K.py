def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

total = int(input("Total Price: "))
print(vatCalculate(total))