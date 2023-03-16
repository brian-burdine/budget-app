from category import Category

# Test 1: Create an instance of the Category Class
def test_category_instance():
    test = Category("Test")
    assert isinstance(test, Category)

# Test 2: Category instance has a "name" property
def test_category_name_exists():
    test = Category("Test")
    assert hasattr(test, "name")

# Test 3: Can set the "name" of a Category object with an argument
def test_category_name_set():
    name = "Utilities"
    utilities = Category(name)
    assert utilities.name == name

# Test 4: Category instance has a "ledger" property
def test_category_ledger_exists():
    food = Category("Food")
    assert hasattr(food, "ledger")

#Test 5: Category instance has a "deposit" method
def test_category_deposit_exists():
    supplies = Category("Art Supplies")
    assert hasattr(supplies, "deposit")

# Test 6: Can add an item to the ledger with Category.deposit()
def test_deposit_an_item():
    gas = Category("Gas")
    starting_length = len(gas.ledger)
    gas.deposit(100)
    current_length = len(gas.ledger)
    assert current_length == starting_length + 1

# Test 7: The ledger contains the amount and description passed to deposit()
def test_deposit_item_stored():
    streaming = Category("Streaming Subscriptions")
    amount = 75
    description = "Monthly Deposit"
    streaming.deposit(amount, description)
    last_item = streaming.ledger[-1]
    assert last_item["amount"] == amount and last_item["description"] == description

# Test 8: If no description is passed, the ledger entry should have an empty string in "description"
def test_deposit_item_with_no_description():
    clothes = Category("New Clothes")
    amount = 100
    clothes.deposit(amount)
    last_item = clothes.ledger[-1]
    assert last_item["amount"] == amount and last_item["description"] == ""

# Test 9: Category instance has a "get_balance" method
def test_category_get_balance_exists():
    phone = Category("Phone Bill")
    assert hasattr(phone, "get_balance")

# Test 10: get_balance returns zero if the ledger is empty
def test_get_balance_when_empty():
    vacation = Category("Dream Trip to Maui!")
    assert vacation.get_balance() == 0

# Test 11: get_balance returns the total amount deposited in ledger
def test_get_balance_with_items():
    savings = Category("Savings Account")
    amount1, amount2, amount3 = 575, 83.40, 921.99
    savings.deposit(amount1)
    savings.deposit(amount2)
    savings.deposit(amount3)
    assert savings.get_balance() == amount1 + amount2 + amount3

# Test 12: Category instance has a "check_funds" method
def test_category_check_funds_exists():
    parking = Category("Parking Fees")
    assert hasattr(parking, "check_funds")

# Test 13: check_funds returns True when amount passed is less than or 
# equal to current balance
def test_check_funds_under():
    music = Category("Music Streaming & Purchase Budget")
    music.deposit(45, "Montly Allowance")
    assert music.check_funds(9.99)

# Test 14: check_funds returns False when amount passed is more than 
# current balance
def test_check_funds_over():
    card = Category("Credit Card Reserved Funds")
    card.deposit(100)
    assert card.check_funds(150) == False
