import auth
import bus
import attendance

def main_menu():
    print("\n===== BusBuddy - College Bus & Attendance Helper =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def user_menu(current_user):
    print(f"\n===== Welcome, {current_user.name} ({current_user.college_id}) =====")
    print("1. View all bus routes")
    print("2. View route details")
    print("3. Search bus by stop name")
    print("4. Mark today’s attendance")
    print("5. View attendance summary")
    print("6. Logout")

def main():
    current_user = None

    while True:
        if current_user is None:
            main_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                auth.register()
            elif choice == "2":
                user = auth.login()
                if user:
                    current_user = user
            elif choice == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            user_menu(current_user)
            choice = input("Choose an option: ").strip()

            if choice == "1":
                bus.list_routes()
            elif choice == "2":
                bus.show_route_details()
            elif choice == "3":
                bus.search_by_stop()
            elif choice == "4":
                attendance.mark_attendance(current_user)
            elif choice == "5":
                attendance.view_summary(current_user)
            elif choice == "6":
                print("Logged out.")
                current_user = None
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
