
class BankAccount:
    def __init__(self, account_id: str, _balance: int = 0, transactions= []) -> None:
        self.account_id = account_id 
        self._balance = _balance
        self.transactions = transactions

    @property
    def _balance(self) -> int:
        return self._balance
    
    def info_save(self, func) -> None:
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            self.transactions.append(result)
            return result
        return wrapper
    
    @info_save
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Can't deposit zero or nagative amount.")
        self._balance += amount

    @info_save
    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("no enough money.")
        if amount <= 0:
            raise ValueError("Can't withdraw zero or nagative amount.")
        self._balance -= amount

    def get_statement():
        ...

    