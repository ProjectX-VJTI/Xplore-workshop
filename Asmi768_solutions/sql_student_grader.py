"""
SQL Based Student Grader CLI
Author: Asmi Mohan

This program allows CRUD operations on student grades
using SQLite3 with proper normalization.

Tables:
1. students
2. subjects
3. grades (composite primary key)
"""

import sqlite3


# -----------------------------
# Database Setup
# -----------------------------

def create_connection():
    return sqlite3.connect("student_grader.db")


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL
        )
    """)

    # Subjects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id INTEGER PRIMARY KEY,
            subject_name TEXT NOT NULL
        )
    """)

    # Grades table (Composite Key)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            student_id INTEGER,
            subject_id INTEGER,
            grade REAL,
            status TEXT,
            PRIMARY KEY (student_id, subject_id),
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# CRUD OPERATIONS
# -----------------------------

def add_student():
    conn = create_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")

    cursor.execute("INSERT OR IGNORE INTO students VALUES (?, ?)",
                   (student_id, student_name))

    conn.commit()
    conn.close()
    print("Student added successfully.")


def add_subject():
    conn = create_connection()
    cursor = conn.cursor()

    subject_id = int(input("Enter Subject ID: "))
    subject_name = input("Enter Subject Name: ")

    cursor.execute("INSERT OR IGNORE INTO subjects VALUES (?, ?)",
                   (subject_id, subject_name))

    conn.commit()
    conn.close()
    print("Subject added successfully.")


def add_grade():
    conn = create_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    subject_id = int(input("Enter Subject ID: "))
    grade = float(input("Enter Grade: "))

    status = "Pass" if grade >= 40 else "Fail"

    try:
        cursor.execute("""
            INSERT INTO grades VALUES (?, ?, ?, ?)
        """, (student_id, subject_id, grade, status))

        conn.commit()
        print("Grade added successfully.")

    except sqlite3.IntegrityError:
        print("Entry already exists or foreign key missing.")

    conn.close()


def view_grades():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.student_name, s.student_id,
               sub.subject_name, sub.subject_id,
               g.grade, g.status
        FROM grades g
        JOIN students s ON g.student_id = s.student_id
        JOIN subjects sub ON g.subject_id = sub.subject_id
    """)

    rows = cursor.fetchall()

    print("\n--- Student Grades ---")
    for row in rows:
        print(row)

    conn.close()


def update_grade():
    conn = create_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    subject_id = int(input("Enter Subject ID: "))
    new_grade = float(input("Enter New Grade: "))

    status = "Pass" if new_grade >= 40 else "Fail"

    cursor.execute("""
        UPDATE grades
        SET grade = ?, status = ?
        WHERE student_id = ? AND subject_id = ?
    """, (new_grade, status, student_id, subject_id))

    conn.commit()
    conn.close()
    print("Grade updated successfully.")


def delete_grade():
    conn = create_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    subject_id = int(input("Enter Subject ID: "))

    cursor.execute("""
        DELETE FROM grades
        WHERE student_id = ? AND subject_id = ?
    """, (student_id, subject_id))

    conn.commit()
    conn.close()
    print("Grade deleted successfully.")


# -----------------------------
# CLI MENU
# -----------------------------

def menu():
    while True:
        print("\n===== SQL Student Grader =====")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Add Grade")
        print("4. View Grades")
        print("5. Update Grade")
        print("6. Delete Grade")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_subject()
        elif choice == "3":
            add_grade()
        elif choice == "4":
            view_grades()
        elif choice == "5":
            update_grade()
        elif choice == "6":
            delete_grade()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    create_tables()
    menu()