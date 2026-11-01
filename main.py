
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "records.json"


# Load records from JSON file
def load_records():
    try:
        if not DATA_FILE.exists():
            return []

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)

            if not isinstance(records, list):
                raise ValueError("Invalid records file format.")

            return records

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print("Error loading records:", error)
        return []


# Save records to JSON file
def save_records(records):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        return True

    except OSError as error:
        print("Error saving records:", error)
        return False


# Get non-empty input
def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty!")


# Add a new student record
def add_record(records):
    print("\n--- Add Student Record ---")

    student_id = get_non_empty_input("Enter Student ID: ")

    for record in records:
        if record["student_id"].lower() == student_id.lower():
            print("Student ID already exists!")
            return

    name = get_non_empty_input("Enter Student Name: ")
    course = get_non_empty_input("Enter Course: ")

    try:
        age = int(input("Enter Age: "))

        if age <= 0:
            print("Age must be positive!")
            return

    except ValueError:
        print("Please enter a valid age!")
        return

    student = {
        "student_id": student_id,
        "name": name,
        "course": course,
        "age": age
    }

    records.append(student)

    if save_records(records):
        print("Student record added successfully!")


# View all records
def view_records(records):
    print("\n--- All Student Records ---")

    if not records:
        print("No records found!")
        return

    print("-" * 65)
    print(f"{'ID':<15}{'Name':<20}{'Course':<20}{'Age':<8}")
    print("-" * 65)

    for student in records:
        print(
            f"{student['student_id']:<15}"
            f"{student['name']:<20}"
            f"{student['course']:<20}"
            f"{student['age']:<8}"
        )

    print("-" * 65)


# Search student record
def search_record(records):
    print("\n--- Search Student Record ---")

    student_id = get_non_empty_input("Enter Student ID: ")

    for student in records:
        if student["student_id"].lower() == student_id.lower():

            print("\nStudent Found!")
            print("ID:", student["student_id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Age:", student["age"])
            return

    print("Student record not found!")


# Update student record
def update_record(records):
    print("\n--- Update Student Record ---")

    student_id = get_non_empty_input("Enter Student ID: ")

    for student in records:
        if student["student_id"].lower() == student_id.lower():

            print("Press Enter to keep the current value.")

            name = input(
                f"Enter New Name [{student['name']}]: "
            ).strip()

            course = input(
                f"Enter New Course [{student['course']}]: "
            ).strip()

            age = input(
                f"Enter New Age [{student['age']}]: "
            ).strip()

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if age:
                try:
                    new_age = int(age)

                    if new_age <= 0:
                        print("Age must be positive!")
                        return

                    student["age"] = new_age

                except ValueError:
                    print("Invalid age!")
                    return

            if save_records(records):
                print("Record updated successfully!")

            return

    print("Student record not found!")


# Delete student record
def delete_record(records):
    print("\n--- Delete Student Record ---")

    student_id = get_non_empty_input("Enter Student ID: ")

    for student in records:
        if student["student_id"].lower() == student_id.lower():

            confirm = input(
                "Are you sure you want to delete this record? (y/n): "
            ).lower()

            if confirm == "y":
                records.remove(student)

                if save_records(records):
                    print("Record deleted successfully!")

            else:
                print("Delete operation cancelled.")

            return

    print("Student record not found!")


# Display application menu
def display_menu():
    print("\n========== STUDENT RECORD MANAGEMENT ==========")
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Search Student Record")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")
    print("================================================")


# Main application
def main():

    records = load_records()

    while True:

        display_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_record(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            search_record(records)

        elif choice == "4":
            update_record(records)

        elif choice == "5":
            delete_record(records)

        elif choice == "6":
            print("Thank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Program execution
if __name__ == "__main__":
    main()
