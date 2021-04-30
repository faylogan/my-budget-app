class Category:

    #constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        #this should return a boolean, it checks if amount is less or greater than self.amount
        return False

    def withdraw(self, amount):
        #reverse of deposit
        self.amount -= amount
        return "You have successfully withdrawn {} in {} category".format(amount, self.category)


    def transfer(self, amount, category):
        #transfer between two instantiated categories
        return self.withdraw(amount) + ' ' + category.deposit(amount)


food_category = Category("Food", 600)
clothing_category = Category("Clothing", 200)
car_category = Category("Car Payment", 500)
miscellaneous_category = Category("Miscellaneous", 400)

#print(food_category.deposit(250))
#print(food_category.budget_balance())
print(food_category.check_balance(60))
#print(food_category.withdraw(200))
#print(clothing_category.budget_balance())
#print(miscellaneous_category.transfer(100, car_category))
