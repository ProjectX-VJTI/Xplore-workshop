"""Practice inheritance."""

from typing import List

class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I am {self.name}"


class Employee(Person):

    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def greet(self) -> str:
        return f"Hi, I am {self.name} and my id is {self.employee_id}"


class Manager(Employee):

    def __init__(self, name: str, age: int, employee_id: str, team: List[Employee] = None):
        super().__init__(name, age, employee_id)
        self.team = team or []

    def add_member(self, employee: Employee):
        self.team.append(employee)

    def team_size(self) -> int:
        return len(self.team)