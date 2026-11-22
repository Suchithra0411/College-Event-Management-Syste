# College Event Management System
# Member 2: Display Events

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

events = [
    {
        "ID": "E101",
        "Name": "Tech Fest",
        "Date": "25-11-2026",
        "Venue": "College Auditorium"
    }
]

display_events(events) 