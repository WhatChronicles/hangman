import sqlite3

conn = sqlite3.connect('myydatabase.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    email TEXT,
    age INTEGER,
    role TEXT CHECK(role IN ('user', 'admin'))
)
''')
conn.commit()

def display_users():
    cursor.execute("SELECT username, email, age, role FROM users")
    users = cursor.fetchall()
    if users:
        for row in users:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    else:
        print("No users found.")


def add_user():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    age_input = input("Age: ")
    role = input("Role (user/admin): ")
    try:
        age = int(age_input)
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
                       (username, password, email, age, role))
        conn.commit()
        print(f"User '{username}' added.")
    except ValueError:
        print("Invalid age.")
    except sqlite3.IntegrityError:
        print("Username already exists.")

def update_user():
    username = input("Username to update: ")
    email = input("New Email: ")
    age_input = input("New Age: ")
    try:
        age = int(age_input)
        cursor.execute("UPDATE users SET email=?, age=? WHERE username=?",
                       (email, age, username))
        conn.commit()
        print(f"Updated '{username}'.")
    except ValueError:
        print("Invalid age.")


def delete_user():
    username = input("Username to delete: ")
    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    print(f"User '{username}' deleted.")

def admin_panel():
    while True:
        print("\n=== ADMIN PANEL ===")
        print("1. Display Users")
        print("2. Add User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit Panel")
        choice = input("Select option: ")

        if choice == '1':
            display_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


def user_input_panel():
    while True:
        print("\n--- USER REGISTRATION ---")
        username = input("Enter your username (or type 'exit' to stop): ")
        if username.lower() == 'exit':
            break

        cursor.execute("SELECT username FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            print("Username already exists.")
            continue

        password = input("Enter your password: ")
        if password.lower() == 'exit':
            break

        email = input("Enter your email: ")
        if email.lower() == 'exit':
            break

        age_input = input("Enter your age: ")
        if age_input.lower() == 'exit':
            break

        try:
            age = int(age_input)
            cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, 'user')",
                           (username, password, email, age))
            conn.commit()
            print("Your data has been submitted.")
        except ValueError:
            print("Invalid age.")
        except sqlite3.IntegrityError:
            print("Error saving data.")

def main_panel():
    while True:
        print("\n--- MAIN PANEL ---")
        identity = input("Are you an 'admin' or 'user'? Type your role or 'exit' to quit: ").strip().lower()

        if identity == 'exit':
            print("Session ended.")
            break
        elif identity == 'admin':
            password = input("Enter admin password: ")
            if password == 'nimda':
                admin_panel()
            else:
                print("Incorrect password. Access denied.")
        elif identity == 'user':
            user_input_panel()
        else:
            print("Invalid role.")

main_panel()