# start of project
class ParkingGarage():
    def __init__(self):
        self.spots = [""] * 20
        self.num_open_spots = 20
    def take_ticket(self):
        if self.num_open_spots == 0:
            print("Sorry, the parking garage is full.")
        else:
            for nm_spot, spot in enumerate(self.spots):
                if not spot:
                    name = input("Please enter your name: ")
                    self.spots[nm_spot] = name
                    self.num_open_spots -= 1
                    print(f"Thank you, {name}. Here is your ticket.")
                    break
    def pay_for_parking(self):
        name = input("Please enter the name on your ticket: ")
        if name in self.spots:
            print("Please pay $1 to exit the garage.")
            self.spots[self.spots.index(name)] = ""
            self.num_open_spots += 1
            print("Thank you for your payment. Have a nice day!")
        else:
            print("Sorry, we could not find your ticket, please check your spelling on your ticket and choose option 2 again.")
    def show_open_spots(self):
        print(f"There are {self.num_open_spots} open spots in the garage.")
    def tkn_spots(self):
        print(f"The following spots are filled in the garage:")
        for num_spot, spot in enumerate(self.spots):
            if spot:
                print(f"Spot {num_spot+1}: {spot}")
        print(f"The following spots are open:")
        for num_spot, spot in enumerate(self.spots):
            if not spot:
                print(f"Spot {num_spot+1}: Open")
    def show_menu(self):
        print("Welcome to the Smith St. parking garage!")
        while True:
            print("Please make a choice from the following options:")
            print("1. Take a ticket")
            print("2. Pay for parking")
            print("3. Show number of empty spots")
            print("4. Show emty and taken spots")
            print("5. Quit")
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.take_ticket()
            elif choice == "2":
                self.pay_for_parking()
            elif choice == "3":
                self.show_open_spots()
            elif choice == "4":
                self.tkn_spots()
            elif choice == "5":
                print("Thank you for using the Smith St. parking garage.")
                break
            else:
                print("Invalid entry, check your menu choice and try again.")
garage = ParkingGarage()
garage.show_menu()