# College Event Management System
# Member 4: Display Registrations

def display_registrations(registrations):

    print("\n--- Registered Participants ---")

    if len(registrations) == 0:
        print("No registrations available.")
        return

    for registration in registrations:
        print("\nStudent Name:", registration["Name"])
        print("Student USN:", registration["USN"])
        print("Event ID:", registration["Event ID"])

registrations = [
    {
        "Name": "Kabilesh",
        "USN": "1AY25CD030",
        "Event ID": "E101"
    }
]

display_registrations(registrations)
