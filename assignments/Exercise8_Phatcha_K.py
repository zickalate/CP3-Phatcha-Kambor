water = 10
melon = 15
hat = 100
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("------Welcome to kShop------")
    print("1. Water 10 THB")
    print("2. Melon 15 THB")
    print("3. Hat 100 THB")
    userSelected = int(input("กรุณาเลือกหมายเลขสินค้าที่ต้องการ : "))
    if userSelected == 1:
        totalSelected = int(input("จำนวนที่ต้องการ : "))
        print("ราคารวมทั้งหมด", water*totalSelected, "บาท")
    elif userSelected == 2:
        totalSelected = int(input("จำนวนที่ต้องการ : "))
        print("ราคารวมทั้งหมด", melon*totalSelected, "บาท")
    elif userSelected == 3:
        totalSelected = int(input("จำนวนที่ต้องการ : "))
        print("ราคารวมทั้งหมด", hat*totalSelected, "บาท")
    print("Thank you :D")
else:
    print("Error! Please try again")
