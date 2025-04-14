import json
import os

FILENAME = "sample1.txt"

# Load employee data from file
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

# Save employee data to file
def save_data(employees):
    with open(FILENAME, "w") as f:
        json.dump(employees, f, indent=4)

def display_menu():
    print("\n***** Employee Management System *****")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Activate/Inactivate Employee")
    print("4. View Employees")
    print("5. Delete Employee")
    print("6. Exit")

def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("\nEmployee ID already exists!\n")
        return

    name = input("Enter Employee Name: ")
    email = input("Enter Employee Email: ")
    phone = input("Enter Employee Phone Number: ")
    department = input("Enter Employee Department: ")
    designation = input("Enter Employee Designation: ")
    status = "Active"  # Default status

    employees[emp_id] = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Department": department,
        "Designation": designation,
        "Status": status
    }

    save_data(employees)
    print(f"\nEmployee {name} (ID: {emp_id}) added successfully!\n")

def search_employee(employees):
    emp_id = input("\nEnter Employee ID to search: ")
    if emp_id in employees:
        print("\nEmployee Found:")
        for key, value in employees[emp_id].items():
            print(f"{key}: {value}")
    else:
        print("\nEmployee Not Found!")

def update_employee_status(employees):
    emp_id = input("\nEnter Employee ID: ")
    if emp_id in employees:
        status = input("Enter Employee Status (Active/Inactive): ").capitalize()
        if status not in ["Active", "Inactive"]:
            print("\nInvalid Status! Choose either 'Active' or 'Inactive'.\n")
            return

        employees[emp_id]["Status"] = status
        save_data(employees)
        print(f"\nEmployee {emp_id} status updated to {status}\n")
    else:
        print("\nEmployee Not Found!")

def view_employees(employees):
    if employees:
        print(f"\n{'ID':<10}{'Name':<20}{'Email':<25}{'Phone':<15}{'Dept':<15}{'Designation':<20}{'Status':<10}")
        print("-" * 115)
        for emp_id, details in employees.items():
            print(f"{emp_id:<10}{details['Name']:<20}{details['Email']:<25}{details['Phone']:<15}"
                  f"{details['Department']:<15}{details['Designation']:<20}{details['Status']:<10}")
    else:
        print("\nNo employees found!\n")

def delete_employee(employees):
    emp_id = input("\nEnter Employee ID to delete: ")
    if emp_id in employees:
        confirm = input(f"Are you sure you want to delete Employee ID {emp_id}? (yes/no): ").lower()
        if confirm == "yes":
            del employees[emp_id]
            save_data(employees)
            print(f"\nEmployee ID {emp_id} deleted successfully!\n")
        else:
            print("\nDeletion canceled.\n")
    else:
        print("\nEmployee Not Found!")

# Load data at start
employees = load_data()

# Main loop
while True:
    display_menu()
    choice = input("Select an option between 1-6: ")

    if choice == '1':
        add_employee(employees)
    elif choice == '2':
        search_employee(employees)
    elif choice == '3':
        update_employee_status(employees)
    elif choice == '4':
        view_employees(employees)
    elif choice == '5':
        delete_employee(employees)
    elif choice == '6':
        print("\nExiting Employee Management System...!")
        break
    else:
        print("\nInvalid choice! Please select a valid option.\n")
