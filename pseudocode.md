# OOP Budget App

## Goals

Design an application in Python that tracks various categories of a budget. Create a **Category** class that accepts a *name* as an initial argument, and creates a *ledger* property. **Category** objects should have methods to add funds to the *ledger*, withdraw them, get the current balance, check if a total exceeds the current balance, and transfer funds from itself to another **Category**. It should also have a method to stringify the object.

## Category
- *name*
  - A string containing the name of the budget category
  - Set by the constructor when the object is instantiated
- *ledger*
  - A list of transactions made in a budget category
  - Initially empty
  - Transactions are added to *ledger* as dicts, with:
    - *amount*: a floating point number, the dollar amount of the transaction
    - *description*: a string that describes the type of transaction
      - A description is optional for the **deposit** and **withdraw** methods, in which case *description* will be an empty string
- *balance*
  - A floating point number, representing the current balance of the budget category
  - Inititially zero
  - Calculated by summing up the deposits and withdrawals stored in *ledger* (transfers are treated as withdrawals, and withdrawals are stored as negative numbers)
- __init__
  - Receives a *name* as an argument
  - Procedure:
    1. start __init__
    2. get *name*
    3. set the object's *name* to *name*
    4. set the object's *ledger* to an empty list
    5. set the object's *balance* to 0.00
    6. end __init__
- __str__
  - Defines a string using the object's properties when the object is used as a string, like in a `print` statement
  - Procedure:
    1. start __str__
    2. init *str* as the object's *name*, centered between asterisks (*) until it fills 30 characters, plus a new line character (\n)
    3. for every item in *ledger*
       1. init *new_line* as the item's *description* followed by *amount*, formatted to have two decimal places
       2. add *new_line* and a new line character to *str*
       3. **TO-DO**: figure out how to constain or pad the *description* so that *new_line* is 30 characters long
    4. endfor
    5. init *final_line* as "Total:" plus the object's *balance*, formatted to have two decimal places
    6. add *final_line* to *str*
    7. return *str*
- **deposit**
  - Receives an *amount* and optionally a *description* as an argument
- **withdraw**
- **get_balance**
- **transfer**
- **check_funds**