class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category_instance.name}')
            category_instance.deposit(
                amount, f'Transfer from {self.name}'
            )
            return True
        return False

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}"[:7].rjust(7)
            items += f'{desc}{amt}\n'
        total = f'Total: {self.get_balance():.2f}'
        return title + items + total


def create_spend_chart(categories):
    # 1. Calculate withdrawals for each category
    spendings = []
    for cat in categories:
        spent = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        spendings.append(spent)

    total_spent = sum(spendings)

    # Calculate percentages rounded down to the nearest 10
    percentages = []
    if total_spent == 0:
        percentages = [0 for _ in categories]
    else:
        for spent in spendings:
            percent = (spent / total_spent) * 100
            rounded = (int(percent // 10)) * 10
            percentages.append(rounded)

    # 2. Build the bar chart string from 100 down to 0
    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += f'{i:3}| '
        for p in percentages:
            if p >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'

    # 3. Horizontal line below bars
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    # 4. Vertical category names
    names = [cat.name for cat in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += '     '
        for name in names:
            if i < len(name):
                chart += name[i] + '  '
            else:
                chart += '   '
        if i < max_length - 1:
            chart += '\n'

    return chart