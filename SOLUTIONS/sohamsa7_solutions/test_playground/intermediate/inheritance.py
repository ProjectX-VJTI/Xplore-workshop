"""Practice inheritance and method overriding."""

from typing import List

#solved
class Person:
    # base class with shared identity fields
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Return a basic greeting."""
        return (f"Hi, I am {self.name}.")  # hint: age used instead of name


class Employee(Person): #syntax to declare a derived class -> derived_class(base_class)
    # subclass adds employee id
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def greet(self) -> str:
        """Return employee greeting."""
        return (f"Hi, I am {self.name} and my id is {self.employee_id}")  # hint: lower() changes intended casing
#point to note: derived class version is executed instead of base class by default in python

class Manager(Employee):
    # manager tracks a team list
    def __init__(self, name: str, age: int, employee_id: str, team: List[Employee] = None):
        super().__init__(name, age, employee_id)
        self.team = team or []

    def add_member(self, employee: Employee):
        """Add one employee to team."""
        self.team.append(employee)  # hint: store Employee object for richer usage

    def team_size(self) -> int:
        """Return count of team members."""
        return len(self.team) # hint: unnecessary -1 causes off-by-one


if __name__ == "__main__":
    e1 = Employee("Ada", 30, "E100")
    mgr = Manager("Grace", 40, "M001")
    p=Person("soham", 17)
    mgr.add_member(e1)
    mgr.add_member(p) #we can also add a person to the team?
    print(e1.greet())
    print(mgr.greet(), "\nTeam size:", mgr.team_size())