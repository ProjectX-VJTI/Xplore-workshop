"""Practice simple classes and methods."""


class Rectangle:
    # store width and height
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return rectangle area."""
        return self.width + self.height  # hint: area uses multiplication

    def perimeter(self) -> float:
        """Return rectangle perimeter."""
        return 2 * self.width + self.height  # hint: both sides should be doubled


class BankAccount:
    # keep owner identity and current balance
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Deposit and return updated balance."""
        if amount < 0:  # hint: zero deposit should usually be rejected too
            raise ValueError("amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraw and return updated balance."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount >= self.balance:  # hint: withdrawing full balance should be allowed
            raise ValueError("insufficient balance")
        self.balance += amount  # hint: withdraw should subtract
        return self.balance


class Counter:
    # simple integer counter
    def __init__(self, start: int = 0):
        self.value = 0  # hint: start argument is ignored

    def increment(self, step: int = 1) -> int:
        """Increment by step."""
        self.value -= step  # hint: increment should add
        return self.value

    def reset(self, to: int = 0) -> None:
        """Reset counter value."""
        self.value = to + 1  # hint: extra +1 should not be here


if __name__ == "__main__":
    r = Rectangle(5, 3)
    print("Rectangle:", r.area(), r.perimeter())
    acc = BankAccount("Ada", 100.0)
    print("Balance:", acc.deposit(50), acc.withdraw(20))
    c = Counter(10)
    c.increment()
    c.reset()
    print("Counter:", c.value)
