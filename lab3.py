# #class Employee:
#     def __init__(self, firstName, lastName, age, salary):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age
#         self.salary = salary
#
#     def __str__(self):
#         return (f"Pracownik {self.firstName} {self.lastName}, wiek: {self.age}, zarobki: {self.salary}")
#
#     def __repr__(self):
#         return (f"Pracownik(Imie={self.firstName}, nazwisko={self.lastName}, wiek={self.age}, zarobki={self.salary})")
#
#
# if __name__ == "__main__":
#     employee = Employee("Jan", "Kowalski", 30, 5000)
#     print(employee)
#     print(repr(employee))
#
#
# class EmployeesManager:
#     def __init__(self):
#         self.employees = []
#
#     def add_employee(self, employee):
#         self.employees.append(employee)
#
#     def get_all_employees(self):
#         return [str(emp) for emp in self.employees]
#
#     def remove_employees_by_age_range(self, min_age, max_age):
#         self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
#
#     def find_employee(self, firstName, lastName):
#         for emp in self.employees:
#             if emp.firstName == firstName and emp.lastName == lastName:
#                 return emp
#         return None
#
#     def update_salary(self, firstName, lastName, new_salary):
#         employee = self.find_employee(firstName, lastName)
#         if employee:
#             employee.salary = new_salary
#             return True
#         return False
#
#
# class FrontendManager:
#     def __init__(self, manager):
#         self.manager = manager
#
#     def display_menu(self):
#         print("1. Dodaj pracownika")
#         print("2. Wyświetl wszystkich pracowników")
#         print("3.  Usuń pracownika sortując według wieku")
#         print("4. Znajdź pracownika")
#         print("5. Zaaktualizuj zarobki pracownika")
#         print("6. Exit")
#
#     def run(self):
#         while True:
#             self.display_menu()
#             choice = input("Wybierz opcje: ")
#             if choice == '1':
#                 firstName = input("Wprowadź imię: ")
#                 lastName = input("Wprowadź nazwisko: ")
#                 age = int(input("Wprowadź wiek: "))
#                 salary = float(input("Wprowadź zarobki: "))
#                 employee = Employee(firstName, lastName, age, salary)
#                 self.manager.add_employee(employee)
#             elif choice == '2':
#                 employees = self.manager.get_all_employees()
#                 for emp in employees:
#                     print(emp)
#             elif choice == '3':
#                 min_age = int(input("Wprowadź minimalny wiek: "))
#                 max_age = int(input("Wprowadź maksymalny wiek: "))
#                 self.manager.remove_employees_by_age_range(min_age, max_age)
#             elif choice == '4':
#                 firstName = input("Wprowadź imię: ")
#                 lastName = input("Wprowadź nazwisko: ")
#                 employee = self.manager.find_employee(firstName, lastName)
#                 if employee:
#                     print(employee)
#                 else:
#                     print("Pracownik nie znaleziony.")
#             elif choice == '5':
#                 firstName = input("Wprowadź imię: ")
#                 lastName = input("Wprowadź nazwisko: ")
#                 new_salary = float(input("Wprowadź nowe zarobki: "))
#                 if self.manager.update_salary(firstName, lastName, new_salary):
#                     print("Zarobki zaktualizowane poprawnie.")
#                 else:
#                     print("Pracownik nie znaleziony.")
#             elif choice == '6':
#                 break
#             else:
#                 print("Zły wybór. Spróbuj ponownie.")
#
#
#
# if __name__ == "__main__":
#     manager = EmployeesManager()
#     frontend = FrontendManager(manager)
#     frontend.run()


import json

class Employee:
    def __init__(self, firstName, lastName, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik {self.firstName} {self.lastName}, wiek: {self.age}, zarobki: {self.salary}"

    def to_dict(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "age": self.age,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["firstName"], data["lastName"], data["age"], data["salary"])


class EmployeesManager:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Employee.from_dict(emp) for emp in data]
        except FileNotFoundError:
            return []

    def save_employees(self):
        with open(self.filename, "w") as file:
            json.dump([emp.to_dict() for emp in self.employees], file)

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employees()

    def get_all_employees(self):
        return [str(emp) for emp in self.employees]

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_employees()

    def find_employee(self, firstName, lastName):
        for emp in self.employees:
            if emp.firstName == firstName and emp.lastName == lastName:
                return emp
        return None

    def update_salary(self, firstName, lastName, new_salary):
        employee = self.find_employee(firstName, lastName)
        if employee:
            employee.salary = new_salary
            self.save_employees()
            return True
        return False


class FrontendManager:
    def __init__(self, manager):
        self.manager = manager

    def login(self):
        username = input("Wprowadź login: ")
        password = input("Wprowadź hasło: ")
        return username == "admin" and password == "aha23"

    def display_menu(self):
        print("1. Dodaj pracownika")
        print("2. Wyświetl wszystkich pracowników")
        print("3. Usuń pracownika według wieku")
        print("4. Znajdź pracownika")
        print("5. Zaaktualizuj zarobki pracownika")
        print("6. Exit")

    def run(self):
        if not self.login():
            print("Błędna próba zalogowania się.")
            return

        while True:
            self.display_menu()
            choice = input("Wybierz opcję: ")
            if choice == '1':
                firstName = input("Wprowadź imie: ")
                lastName = input("Wprowadź nazwisko: ")
                age = int(input("Wprowadź wiek: "))
                salary = float(input("Wprowdź zarobki: "))
                employee = Employee(firstName, lastName, age, salary)
                self.manager.add_employee(employee)
            elif choice == '2':
                employees = self.manager.get_all_employees()
                for emp in employees:
                    print(emp)
            elif choice == '3':
                min_age = int(input("Wprowadź minimalny wiek: "))
                max_age = int(input("Wprowadź maksymalny wiek: "))
                self.manager.remove_employees_by_age_range(min_age, max_age)
            elif choice == '4':
                firstName = input("Wprowadź imię: ")
                lastName = input("Wprowadź nazwisko: ")
                employee = self.manager.find_employee(firstName, lastName)
                if employee:
                    print(employee)
                else:
                    print("Pracownik nie znaleziony.")
            elif choice == '5':
                firstName = input("Wprowadź imie: ")
                lastName = input("Wprowadź nazwisko: ")
                new_salary = float(input("Wprowadź nowe zarobki: "))
                if self.manager.update_salary(firstName, lastName, new_salary):
                    print("Zarobki zaaktualizowane pomyślnie.")
                else:
                    print("Pracownik nie znaleziony.")
            elif choice == '6':
                break
            else:
                print("Zły wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    manager = EmployeesManager()
    frontend = FrontendManager(manager)
    frontend.run()
