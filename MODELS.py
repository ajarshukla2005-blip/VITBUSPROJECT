class User:
    def __init__(self, name, email, password, college_id):
        self.name = name
        self.email = email
        self.password = password
        self.college_id = college_id

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "college_id": self.college_id
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            college_id=data["college_id"]
        )


class BusRoute:
    def __init__(self, route_id, start, end, stops):
        self.route_id = route_id
        self.start = start
        self.end = end
        self.stops = stops  # list of dicts: {"name": , "time": }

    @staticmethod
    def from_dict(data):
        return BusRoute(
            route_id=data["route_id"],
            start=data["start"],
            end=data["end"],
            stops=data["stops"]
        )


class AttendanceRecord:
    def __init__(self, email, date_str, status):
        self.email = email
        self.date_str = date_str  # "YYYY-MM-DD"
        self.status = status      # "Present" or "Absent"

    def to_dict(self):
        return {
            "email": self.email,
            "date": self.date_str,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return AttendanceRecord(
            email=data["email"],
            date_str=data["date"],
            status=data["status"]
        )
