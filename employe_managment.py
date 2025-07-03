import json

# Base Employee class
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        try:
            self.salary = float(salary)
        except ValueError:
            raise ValueError("Salary must be a number.")

    def yearly_salary(self):
        return self.salary * 12

    def display_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}, Salary: {self.salary}")

    def to_dict(self):
        return {
            "type": "Employee",
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }

# Manager subclass
class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, team_size):
        super().__init__(emp_id, name, department, salary)
        self.team_size = int(team_size)

    def bonus(self):
        return 0.1 * self.yearly_salary() if self.team_size > 5 else 0

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}, Bonus: {self.bonus()}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Manager"
        data["team_size"] = self.team_size
        return data

# List to store employee objects
employees = []

# Load data from file
def load_employees():
    try:
        with open("employees.txt", "r") as f:
            data = json.load(f)
            for item in data:
                if item["type"] == "Manager":
                    emp = Manager(item["emp_id"], item["name"], item["department"], item["salary"], item["team_size"])
                else:
                    emp = Employee(item["emp_id"], item["name"], item["department"], item["salary"])
                employees.append(emp)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing data found or file is corrupted.")

# Save data to file
def save_employees():
    with open("employees.txt", "w") as f:
        json.dump([e.to_dict() for e in employees], f)

# Add new employee
def add_employee():
    try:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        emp = Employee(emp_id, name, dept, salary)
        employees.append(emp)
        print("Employee added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

# Add new manager
def add_manager():
    try:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        team_size = int(input("Enter Team Size: "))
        mgr = Manager(emp_id, name, dept, salary, team_size)
        employees.append(mgr)
        print("Manager added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

# Search by ID
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    for emp in employees:
        if emp.emp_id == emp_id:
            emp.display_details()
            found = True
            break
    if not found:
        print("Employee not found.")

# Display summary
def display_summary():
    print("\n--- Employee Summary ---")
    sorted_emps = sorted(employees, key=lambda e: e.salary, reverse=True)
    for emp in sorted_emps:
        emp.display_details()
        print("----------------------")

# Menu
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Add Manager")
        print("3. Search Employee by ID")
        print("4. Display Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            add_manager()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            display_summary()
        elif choice == '5':
            save_employees()
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
if __name__ == "__main__":
    load_employees()
    menu()
