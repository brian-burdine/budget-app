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
    5. end __init__
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
    5. init *final_line* as "Total:" 
    6. call **get_balance**, add the result formatted to have two decimal places to *final_line*
    6. add *final_line* to *str*
    7. return *str*
    8. end __str__
- **deposit**
  - Receives an *amount* and optionally a *description* as an argument
  - Adds funds to the **Category** object's *ledger*, and a description of the deposit if one is provided
  - Procedure:
    1. start **deposit**
    2. get *amount* and *description*
    3. if *description* was passed
       1. add a dictionary with keys "amount" and "description" with values of the passed *amount* and *description* to the end of the object's *ledger* list
    4. else
       1. add a dictionary with keys "amount" and "description" with the value of the passed *amount* and an empty string to the end of the object's ledger list
    5. endif
    6. end **deposit**
- **withdraw**
  - Receives an *amount* and optionally a *description* as an argument
  - Attempts to withdraw funds from the **Category** object's *ledger*; if there are sufficient funds to cover the *amount*, the withdrawal is marked as a negative deposit in the ledger and **withdraw** returns `True`. If not, nothing is added to the *ledger*, and **withdraw** returns `False`.
  - Procedure:
    1. start **withdraw**
    2. get *amount* and *description*
    3. call **check_funds** with *amount* as an argument
    4. if **check_funds** returns `True`
       1. call **deposit** with *amount* multiplied by -1 and *description* as arguments
       2. return `True`
    5. else
       1. return `False`
    6. endif
    7. end **withdraw**
- **get_balance**
  - Gets the current amount of funds in the **Category** object, based on the deposits and withdrawals made
  - Procedure:
    1. start **get_balance**
    2. init *balance* as zero
    3. for every item in *ledger*
       1. add the item's *amount* to *balance*
    4. endfor
    5. return *balance*
    6. end **get_balance**
- **transfer**
  - Receives an *amount* and a *destination*
  - Attempts to transfer funds from **Category** object's balance to the *destination*'s. If there are sufficient funds in the source object's *ledger*, a withdrawal of the *amount* is registered with the description "Transfer to (*destination*'s *name*)", and a deposit of the *amount* is registered in the *destination*'s *ledger* with the description "Transfer from (source's *name*). If the transfer occurred, **transfer** returns `True`; otherwise, it returns `False`.
  - Procedure:
    1. start **transfer**
    2. get *amount* and *destination*
    3. call **check_funds** with *amount* as an argument
    4. if **check_funds** returns `True`
       1. call **withdraw** on the current object, with *amount* and "Transfer to (*destination*'s *name*)" as arguments
       2. call **deposit** on the *destination* object, with *amount* and "Transfer from (current object's *name*) as arguments
       3. return `True`
    5. else
       1. return `False`
    6. endif
    7. end **transfer**
- **check_funds**
  - Receives an *amount* as an argument
  - Checks to see if the passed *amount* is less than or equal to the current balance of the **Category** object. If it is, **check_funds** returns `True`; otherwise, it returns `False`.
  - Procedure:
    1. start **check_funds**
    2. get *amount*
    3. call **get_balance** and store its value in *balance*
    4. if *amount* is less than or equal to *balance*
       1. return `True`
    5. else
       2. return `False`
    6. endif
    7. end **check_funds**