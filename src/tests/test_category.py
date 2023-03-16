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
