# College Event Management System
# Member 4: Display Registrations

def add_registration(registrations):

    print("\n--- Register for Event ---")

    name = input("Enter Student Name: ")
    usn = input("Enter Student USN: ")
    event_id = input("Enter Event ID: ")

    registration = {
        "Name": name,
        "USN": usn,
        "Event ID": event_id
    }

    registrations.append(registration)

    print("\nRegistration successful!")


def display_registrations(registrations):

    print("\n--- Registered Participants ---")

    if len(registrations) == 0:
        print("No registrations available.")
        return

    for registration in registrations:
        print("\nStudent Name:", registration["Name"])
        print("Student USN:", registration["USN"])
        print("Event ID:", registration["Event ID"])


# Main program
registrations = []

add_registration(registrations)
display_registrations(registrations)