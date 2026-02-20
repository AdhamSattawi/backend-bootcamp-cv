from budget import Budget
from actions import add_expense, add_income, view_expense, view_income, view_summary, remove, clear_all


def handle_action(user_option: int, my_budget: Budget):
    if user_option in range(1,3):
        handle_adding(user_option, my_budget)
    elif user_option in range(3,6):
        handle_view(user_option, my_budget)
    elif user_option in range(6,9):
        handle_removing(user_option, my_budget)
    else:
        raise ValueError("Wrong Option, please select the proper number from the list.")

def handle_adding():
    ...

def handle_view():
    ...

def handle_removing():
    ...