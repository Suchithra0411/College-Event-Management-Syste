
# College Event Management System
# Member 1: Create Event

events = []

def create_event():
    print("\n--- Create New Event ---")

    event_id = input("Enter Event ID: ")
    event_name = input("Enter Event Name: ")
    event_date = input("Enter Event Date: ")
    event_venue = input("Enter Event Venue: ")

    event = {
        "ID": event_id,
        "Name": event_name,
        "Date": event_date,
        "Venue": event_venue
    }

    events.append(event)

    print("\nEvent created successfully!")
    print("Event ID:", event["ID"])
    print("Event Name:", event["Name"])
    print("Event Date:", event["Date"])
    print("Event Venue:", event["Venue"])


# Run the function
create_event()
