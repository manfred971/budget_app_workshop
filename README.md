# Budget App

This project implements a small, in-memory budget tracker. It groups deposits
and withdrawals into named spending categories, supports transfers between
categories, and creates a text bar chart showing how total withdrawals are
distributed.

## Requirements

- Python 3. No third-party packages are required.

## Features

### Categories and ledgers

Create a category by passing its name to `Category`. Each category has a
`ledger`, a list of transaction dictionaries containing an `amount` and a
`description`.

- `deposit(amount, description='')` adds a positive transaction.
- `withdraw(amount, description='')` records the amount as negative and
  returns `True` if the category has enough funds; otherwise it returns
  `False` without changing the ledger.
- `get_balance()` returns the sum of the category's ledger amounts.
- `check_funds(amount)` returns whether the current balance can cover the
  amount.
- `transfer(amount, destination)` moves funds to another category and records
  matching transfer descriptions in both ledgers. It returns `True` on success
  and `False` if there are insufficient funds.

Printing a category displays its name centered in a 30-character title,
followed by its ledger entries. Descriptions are limited to 23 characters,
amounts are displayed to two decimal places in a seven-character field, and
the final line shows the category balance.

### Spending chart

`create_spend_chart(categories)` returns a string chart of withdrawals only;
deposits are not counted as spending. Each category's share of the total
spending is rounded down to the nearest 10 percent. The chart labels the
vertical axis from 100 to 0, draws bars using `o`, and prints category names
vertically beneath the chart.

## Usage

Import the classes and function from `budget_app_workshop.py`:

```python
from budget_app_workshop import Category, create_spend_chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
```

To try the example, open a terminal in this directory, start Python, and enter
the code above. The module defines the budget functionality; it does not run a
demo automatically when executed as a script.
