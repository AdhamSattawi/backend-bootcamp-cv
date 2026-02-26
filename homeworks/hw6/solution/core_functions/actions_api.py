from user_interface.user_input import income_input, expense_input, remove_input
import requests
from budget_app_api.budget_planner_api import my_budget

BASE_URL = "http://127.0.0.1:8000"

def add_income() -> None:
    income_amount, income_description = income_input()
    data = {"amount" : income_amount, "description" : income_description}
    requests.post(f"{BASE_URL}/income",data)
    print("Income successfully added!")


def add_expense() -> None:
    expense_amount, expense_description = expense_input()
    data = {"amount" : expense_amount, "description" : expense_description}
    requests.post(f"{BASE_URL}/expense",data)
    print("expense successfully added!")


def view_summary() -> None:
    incomes = my_budget.view_incomes()
    expenses = my_budget.view_expenses()

    print("----------EXPENSES---------")
    summary_data = requests.get(f"{BASE_URL}/summary")
    print(f"""
    All Recorded Incomes: {incomes}
    All Recorded Expenses: {expenses}
    Total Incomes: {summary_data["Total Incomes"]}
    Total Expenses: {summary_data["Total Expenses"]}
    Remaning Budget: {summary_data["Remaning Budget"]}
    +++++++++++++++++++++++++++++++++++++++
    """)


def remove(activity_type: str) -> None:
    id = remove_input()
    requests.delete(f"{BASE_URL}/{activity_type}/{id}")
    print("Successfully Removed!")


def clear_all() -> None:
    requests.delete(f"{BASE_URL}/clear")
    print("All Data Has Been Removed!")
