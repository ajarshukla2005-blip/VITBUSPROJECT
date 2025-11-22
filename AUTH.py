from models import User
import storage

def register():
    print("\n--- Register New User ---")
    name = input("Name: ").strip()
    email = input("Email: ").strip().lower()
    college_id = input("College ID: ").strip()
    password = input("Password (min 4 chars): ").strip()

    if len(password) < 4:
        print("Password too short.")
        return None

    users = storage.load_users()
    for u in users:
        if u["email"] == email:
            print("Email already registered.")
            return None

    new_user = User(name, email, password, college_id)
    users.append(new_user.to_dict())
    storage.save_users(users)
    print("Registration successful. You can now login.")
    return new_user

def login():
    print("\n--- Login ---")
    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    users = storage.load_users()
    for u in users:
        if u["email"] == email and u["password"] == password:
            print(f"Welcome back, {u['name']}!")
            return User.from_dict(u)

    print("Invalid email or password.")
    return None
