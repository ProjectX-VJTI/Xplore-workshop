class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.employee_id}"

class Doctor(Employee):
    def __init__(self, name, age, employee_id, specialization):
        super().__init__(name, age, employee_id)
        self.specialization = specialization

    def perform_duty(self):
        return f"Dr. {self.name} is performing a checkup in {self.specialization}."

class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment

    def get_status(self):
        return f"Patient {self.name} (Age: {self.age}) is admitted for {self.ailment}."

if __name__ == "__main__":
    # Level 2 Inheritance: Person -> Employee -> Doctor
    doc = Doctor("Aaryan", 28, "D742", "Cardiology")
    
    # Level 1 Inheritance: Person -> Patient
    pat = Patient("Rohan", 20, "Viral Fever")

    print("--- Healthcare System Records ---")
    print(doc.get_details())
    print(doc.perform_duty())
    print("-" * 30)
    print(pat.get_details())
    print(pat.get_status())