
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
        if amount <= 0:
            raise ValueError("Income amount must be greater than zero.")
        new_income = Income(amount, description)
        self.incomes[self.income_id] = new_income
        self.income_id += 1
        return new_income

    def add_expense(self, amount: float, description: str) -> Expense:
        """This function adds the expense amount with the description to the budget"""
        if amount <= 0:
            raise ValueError("Income amount must be greater than zero.")
        new_expense = Expense(amount, description)
        self.expenses[self.expense_id] = new_expense
        self.expense_id += 1
        return new_expense

    def view_summary(self) -> tuple:
        """This function shows the summary of the budget"""
        all_incomes = list(self.incomes.values())
        all_expenses = list(self.expenses.values())
        total_income = 0
        for income in all_incomes:
            total_income += income.amount
        total_expense = 0
        for expense in all_expenses:
            total_expense += expense.amount
        remaning_budget = total_income - total_expense
        return (all_incomes, all_expenses, total_income, total_expense, remaning_budget)
    
    def view_incomes(self) -> dict:
        return self.incomes

    def view_expenses(self) -> dict:
        return self.expenses

    def remove_by_id(self, activity_type: str, activity_id: int) -> Income | Expense | None:
        """This function removes a specific expense or income with it's id from the budget"""
        if activity_type.lower() == "income":
            return self.incomes.pop(activity_id, None)
        elif activity_type.lower() == "expense":
            return self.expenses.pop(activity_id, None)
        return None
    
    def remove_by_description(self, activity_type: str, description: str) -> Income | Expense | None:
        """This function removes a specific expense or income with it's description from the budget"""
        search_type = activity_type.lower()
        search_description = description.lower()
        if search_type == "income":
            for key, income in self.incomes.items():
                if search_description in income.description.lower():
                    return self.incomes.pop(key, None)
        elif search_type == "expense":
            for key, expense in self.expenses.items():
                if search_description in expense.description.lower():
                    return self.expenses.pop(key, None)
        return None

    def clear_all(self) -> None:
        """This function clears all the activities from the budget"""
        self.incomes.clear()
        self.expenses.clear()
        return None

