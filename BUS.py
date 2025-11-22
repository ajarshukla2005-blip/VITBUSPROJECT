from models import BusRoute
import storage

def list_routes():
    routes_data = storage.load_bus_routes()
    routes = [BusRoute.from_dict(r) for r in routes_data]

    print("\n--- Available Bus Routes ---")
    for r in routes:
        print(f"{r.route_id}: {r.start} -> {r.end}")
    return routes

def show_route_details():
    routes = list_routes()
    route_id = input("\nEnter route id to view details (e.g. R1): ").strip().upper()
    for r in routes:
        if r.route_id.upper() == route_id:
            print(f"\nRoute {r.route_id}: {r.start} -> {r.end}")
            print("Stops:")
            for s in r.stops:
                print(f"  {s['time']} - {s['name']}")
            return
    print("Route not found.")

def search_by_stop():
    routes_data = storage.load_bus_routes()
    routes = [BusRoute.from_dict(r) for r in routes_data]
    stop_name = input("\nEnter stop name to search: ").strip().lower()

    found = False
    for r in routes:
        for s in r.stops:
            if stop_name in s["name"].lower():
                if not found:
                    print("\n--- Matching Stops ---")
                found = True
                print(f"Route {r.route_id}: {s['name']} at {s['time']} (towards {r.end})")
    if not found:
        print("No matching stop found.")
