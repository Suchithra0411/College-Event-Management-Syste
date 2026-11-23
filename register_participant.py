
# College Event Management System
# Member 3: Register Participant


def register_participant(events, registrations):

    print("\n--- Register for an Event ---")

    if len(events) == 0:
        print("No events available for registration.")
        return

    student_name = input("Enter Student Name: ")
    student_usn = input("Enter Student USN: ")
    event_id = input("Enter Event ID: ")

    # Check whether the event exists
    event_found = False

    for event in events:
        if event["ID"] == event_id:
            event_found = True
            break

    if event_found:
        registration = {
            "Name": student_name,
            "USN": student_usn,
            "Event ID": event_id
        }

        registrations.append(registration)

        print("\nRegistration successful!")
        print("Student Name:", student_name)
        print("Student USN:", student_usn)
        print("Event ID:", event_id)

    else:
        print("Invalid Event ID. Please enter a valid event ID.")
# Main program
events = [
    {"ID": "E101", "Name": "Coding Competition"},
    {"ID": "E102", "Name": "Quiz Competition"}
]

registrations = []

register_participant(events, registrations)
