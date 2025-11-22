
import json
import os

DATA_DIR = "data"

def _ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def _load_json(filename, default):
    _ensure_data_dir()
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        # create file with default data
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # if file is corrupted, just reset it
        return default

def _save_json(filename, data):
    _ensure_data_dir()
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_users():
    return _load_json("users.json", [])

def save_users(users):
    _save_json("users.json", users)

def load_bus_routes():
    # some default routes so app is usable on first run
    default_routes = [
        {
            "route_id": "R1",
            "start": "City Center",
            "end": "College Main Gate",
            "stops": [
                {"name": "City Center", "time": "08:00"},
                {"name": "Market Square", "time": "08:15"},
                {"name": "Tech Park", "time": "08:35"},
                {"name": "College Main Gate", "time": "09:00"}
            ]
        },
        {
            "route_id": "R2",
            "start": "Railway Station",
            "end": "College Main Gate",
            "stops": [
                {"name": "Railway Station", "time": "08:10"},
                {"name": "Bus Stand", "time": "08:25"},
                {"name": "Old Bridge", "time": "08:45"},
                {"name": "College Main Gate", "time": "09:05"}
            ]
        }
    ]
    return _load_json("bus_routes.json", default_routes)

def save_bus_routes(routes):
    _save_json("bus_routes.json", routes)

def load_attendance():
    return _load_json("attendance.json", [])

def save_attendance(records):
    _save_json("attendance.json", records)
