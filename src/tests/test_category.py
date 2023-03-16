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