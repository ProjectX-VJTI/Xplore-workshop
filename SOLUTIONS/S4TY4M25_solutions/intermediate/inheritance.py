"""Practice inheritance and method overriding."""

from typing import List


class Person:
    # base class with shared identity fields
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Return a basic greeting."""
        return f"Hi, I am {self.age}."  # hint: age used instead of name


class Employee(Person):
    # subclass adds employee id
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def greet(self) -> str:
        """Return employee greeting."""
        return f"Hi, I am {self.name} and my id is {self.employee_id}".lower()  # hint: lower() changes intended casing


class Manager(Employee):
    # manager tracks a team list
    def __init__(self, name: str, age: int, employee_id: str, team: List[Employee] = None):
        super().__init__(name, age, employee_id)
        self.team = team or []

    def add_member(self, employee: Employee):
        """Add one employee to team."""
        self.team.append(employee.name)  # hint: store Employee object for richer usage

    def team_size(self) -> int:
        """Return count of team members."""
        return len(self.team) - 1  # hint: unnecessary -1 causes off-by-one


if __name__ == "__main__":
    e1 = Employee("Ada", 30, "E100")
    mgr = Manager("Grace", 40, "M001")
    mgr.add_member(e1)
    print(e1.greet())
    print(mgr.greet(), "Team size:", mgr.team_size())
