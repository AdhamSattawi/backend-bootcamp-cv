
class Income:
    """This class defines the income transaction structure."""
    def __init__(self, amount: float, description: str) -> None:
        self.amount = amount
        self.description = description

class Expense:
    """This class defines the expense transaction structure."""
    def __init__(self, amount: float, description: str) -> None:
        self.amount = amount
        self.description = description

class Budget:
    """This class have all of the operations functions"""
    def __init__(self) -> None:
        self.incomes: dict[int, Income] = {}
        self.expenses: dict[int, Expense] = {}
        self.income_id = 1
        self.expense_id = 1

    def add_income(self, amount: float, description: str) -> Income:
        """This function adds the income amount with the description to the budget"""
        new_income = Income(amount, description)
        self.incomes[self.income_id] = new_income
        self.income_id += 1
        return new_income

    def add_expense(self, amount: float, description: str) -> Expense:
        """This function adds the expense amount with the description to the budget"""
        new_expense = Expense(amount, description)
        self.expenses[self.expense_id] = new_expense
        self.expense_id += 1
        return new_expense

    def view_summary(self):
        """This function shows the summary of the budget"""
        
        ...

    def remove(self):
        """This function removes a specific expense or income amount with it's description from the budget"""

        ...

    def clear_all(self):
        """This function clears all the activities from the budget"""
        ...

