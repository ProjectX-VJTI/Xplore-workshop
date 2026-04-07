"""Practice simple classes and methods."""


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return rectangle area (w * h)."""
        return self.width * self.height 

    def perimeter(self) -> float:
        """Return rectangle perimeter (2 * (w + h))."""
        return 2 * (self.width + self.height)


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Deposit and return updated balance."""
        if amount <= 0:  
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraw and return updated balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:  
            raise ValueError("Insufficient balance")
        self.balance -= amount  
        return self.balance


class Counter:
    def __init__(self, start: int = 0):
        self.value = start  

    def increment(self, step: int = 1) -> int:
        """Increment by step."""
        self.value += step  
        return self.value

    def reset(self, to: int = 0) -> None:
        """Reset counter value."""
        self.value = to


if __name__ == "__main__":
    # Expected: Rectangle Area 15.0, Perimeter 16.0
    r = Rectangle(5, 3)
    print(f"Rectangle: Area={r.area()}, Perimeter={r.perimeter()}")
    
    # Expected: Balance after deposit 150.0, after withdrawal 130.0
    acc = BankAccount("Akshita", 100.0)
    print(f"Account: {acc.owner}'s Balance={acc.deposit(50)} -> {acc.withdraw(20)}")
    
    # Expected: Start at 10, increment to 11, reset to 0
    c = Counter(10)
    c.increment()
    print(f"Counter after increment: {c.value}")
    c.reset()
    print(f"Counter after reset: {c.value}")
