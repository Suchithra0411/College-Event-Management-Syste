# College Event Management System
# Member 2: Display Events

def add_event(events):

    print("\n--- Add New Event ---")

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

    print("\nEvent added successfully!")


def display_events(events):

    print("\n--- Available College Events ---")

    if len(events) == 0:
        print("No events available.")
        return

    for event in events:
        print("\nEvent ID:", event["ID"])
        print("Event Name:", event["Name"])
        print("Event Date:", event["Date"])
        print("Event Venue:", event["Venue"])


# Main program
events = []

add_event(events)
display_events(events)