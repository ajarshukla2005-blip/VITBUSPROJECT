from datetime import date
from models import AttendanceRecord
import storage

def _load_records():
    data = storage.load_attendance()
    return [AttendanceRecord.from_dict(d) for d in data]

def _save_records(records):
    storage.save_attendance([r.to_dict() for r in records])

def mark_attendance(current_user):
    if current_user is None:
        print("You need to login first.")
        return

    today = date.today().isoformat()
    records = _load_records()

    # check if already marked for today
    for r in records:
        if r.email == current_user.email and r.date_str == today:
            print(f"Attendance already marked for today ({today}). Status: {r.status}")
            return

    print(f"\n--- Mark Attendance for {today} ---")
    print("1. Present")
    print("2. Absent")
    choice = input("Choose (1/2): ").strip()

    status = "Present" if choice == "1" else "Absent"
    new_record = AttendanceRecord(current_user.email, today, status)
    records.append(new_record)
    _save_records(records)
    print(f"Attendance marked as {status}.")

def view_summary(current_user):
    if current_user is None:
        print("You need to login first.")
        return

    records = _load_records()
    user_records = [r for r in records if r.email == current_user.email]

    if not user_records:
        print("No attendance records found.")
        return

    total = len(user_records)
    present = sum(1 for r in user_records if r.status == "Present")
    absent = total - present
    percentage = (present / total) * 100 if total > 0 else 0

    print("\n--- Attendance Summary ---")
    print(f"Total days marked : {total}")
    print(f"Present           : {present}")
    print(f"Absent            : {absent}")
    print(f"Percentage        : {percentage:.2f}%")

    # small human-like messages
    if percentage >= 90:
        remark = "Excellent, keep it up."
    elif percentage >= 75:
        remark = "Decent, but try not to miss too many classes."
    elif percentage >= 60:
        remark = "Borderline. You should be a bit more regular."
    else:
        remark = "Warning: Attendance is quite low."

    print(f"Remark            : {remark}")
