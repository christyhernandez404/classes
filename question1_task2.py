#Use the existing Event class by adding an instance attribute to keep track of the number of participants. 
# Implement a method add_participant that increases the count 
# and a method get_participant_count to retrieve the current count.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        self.participant_count = 0

    def add_participant(self):
        going_to_event = input("Would you like to register for the event? y/n : ")
        if going_to_event.lower() == 'y':
            full_name = input("Input your first and last name: ")
            print(f"Name: {full_name}, Date: {self.date}")
            correct = input("Is this information accurate? y/n: ")
            if correct.lower() == 'y':
                self.participants.append(full_name)
                self.participant_count += 1
                print(f"You've registered for the {self.name}! See you then!")
        else:
            pass

    def get_participant_count(self):
        return self.participant_count

first_event = Event("Rock Concert",'06/20/2024')

first_event.add_participant()
print(f"Current number of participants: {first_event.get_participant_count()}")