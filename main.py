# College Event Management System
# Main program integrating all 4 members' functions

from create_event import create_event
from display_events import display_events
from register_participant import register_participant
from display_registrations import display_registrations


# Shared lists to store data
events = []
registrations = []


# Main menu
def main():

    while True:

        print("\n===== COLLEGE EVENT MANAGEMENT SYSTEM =====")
        print("1. Create Event")
        print("2. Display Events")
        print("3. Register Participant")
        print("4. Display Registrations")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_event(events)

        elif choice == "2":
            display_events(events)

        elif choice == "3":
            register_participant(events, registrations)

        elif choice == "4":
            display_registrations(registrations)

        elif choice == "5":
            print("Thank you for using College Event Management System!")
            break

        else:
            print("Invalid choice! Please enter 1 to 5.")


# Run the main program
if __name__ == "__main__":
    main()
