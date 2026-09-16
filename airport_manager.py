airport_info = ("OUL", 1, "14-09-2026")

allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}

restricted_destinations = {"Moscow", "Pyongyang"}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}


def find_flight(flights, flight_number):
    if flights is None:
        return None
    normalized = flight_number.strip().upper()
    for key in flights:
        if key.strip().upper() == normalized:
            return key
    return None


def passenger_exists(passengers, passenger_name):
    if passengers is None:
        return False
    name_lower = passenger_name.strip().lower()
    for p in passengers:
        if p.strip().lower() == name_lower:
            return True
    return False


def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    if flights is None:
        return "FLIGHT_NOT_FOUND"

    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    name = passenger_name.strip().title()
    if name == "":
        return "EMPTY_NAME"

    flight = flights[flight_key]

    if passenger_exists(flight["passengers"], name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    flight["passengers"].append(name)
    return "OK"


def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    if flights is None:
        return "FLIGHT_NOT_FOUND"

    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[flight_key]
    passengers = flight["passengers"]
    name_lower = passenger_name.strip().lower()

    for i, p in enumerate(passengers):
        if p.strip().lower() == name_lower:
            passengers.pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    if flights is None:
        return "FLIGHT_NOT_FOUND"

    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    new_gate_upper = new_gate.strip().upper()
    matched_gate = None
    for g in allowed_gates:
        if g.upper() == new_gate_upper:
            matched_gate = g
            break

    if matched_gate is None:
        return "INVALID_GATE"

    flights[flight_key]["gate"] = matched_gate
    return "OK"


def flight_status(flight):
    current = len(flight["passengers"])
    capacity = flight["capacity"]

    if capacity == 0:
        return "AVAILABLE"

    percentage = current / capacity * 100

    if percentage == 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


def sorted_manifest(
    flights,
    flight_number
):
    if flights is None:
        return None

    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return None

    return sorted(flights[flight_key]["passengers"])


def total_passengers(flights):
    if flights is None:
        return 0
    total = 0
    for flight in flights.values():
        total += len(flight["passengers"])
    return total


def any_full_flight(flights):
    if flights is None:
        return False
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True
    return False


def all_flights_have_passengers(flights):
    if flights is None:
        return False
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False
    return True
    pass
