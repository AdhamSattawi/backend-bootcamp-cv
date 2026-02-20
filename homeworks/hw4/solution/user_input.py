def user_selection() -> int:
    option = input("Choose an option: ")
    if not int(option):
        raise ValueError("please enter the option's number.")
    return int(option)