from category import Category

house = Category("Home Improvement")
car = Category("Vehicle Expenses")
groceries = Category("Groceries")
takeout = Category("Eating Out")
games = Category("Games")

house.deposit(2500, "Initial investment")
car.deposit(625)
groceries.deposit(500, "Monthly allotment")
takeout.deposit(16, "Weekly allotment")
games.deposit(75, "Next purchase allowed")

house.withdraw(875, "Roof damage repair")
car.withdraw(36.27, "Gas")
groceries.withdraw(123.45, "Week 1")
takeout.withdraw(11.42, "Drive-Thru")
games.withdraw(74.18, "Hot new game")

takeout.deposit(100, "Big date week")

house.withdraw(499.99, "Deck Chairs")
car.withdraw(930, "Car Broke Down")
house.transfer(930, car)
car.withdraw(930, "Car Broke Down")
groceries.withdraw(64.87, "Week 2")
takeout.withdraw(87.43, "Fancy restaurant")
games.withdraw(18, "Sweet cosmetics")

print(house)
print(car)
print(groceries)
print(takeout)
print(games)