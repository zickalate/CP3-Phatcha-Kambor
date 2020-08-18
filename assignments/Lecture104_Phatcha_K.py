class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to ", self.name, self.lastname, "'s cart")

customer1 = Customer()
customer1.name = "Phatcha"
customer1.lastname = "Kambor"
customer1.addCart()

customer2 = Customer()
customer2.name = "AAA"
customer2.lastname = "BBB"
customer2.addCart()

customer3 = Customer()
customer3.name = "CCC"
customer3.lastname = "DDD"
customer3.addCart()