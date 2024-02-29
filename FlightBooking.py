import random
import json

def generate_Seat_number():
    return ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))

def purchase_ticket():
    name = input("Enter your name: ")
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")
    date = input("Enter travel date (YYYY-MM-DD): ")

    # Generate a random ticket number
    Seat_number = generate_Seat_number()

    ticket_data = {
        'Name': name,
        'Source': source,
        'Destination': destination,
        'Date': date,
        'SeatNumber': Seat_number
    }

    # Save data to a file
    save_Seat_data(ticket_data)

    print("\nTicket purchased successfully!")
    print("Seat Number:", Seat_number)
    print("Enjoy your flight!")

def save_Seat_data(ticket_data):
    try:
        with open('Seat_data.json', 'a') as file:
            json.dump(Seat_data, file)
            file.write('\n')  # Separate entries by a new line
    except Exception as e:
        print("Error saving Seat data:", str(e))

def main():
    print("Welcome to Airplane Ticket Booking System\n")
    purchase_ticket()

if __name__ == "__main__":
    main()
