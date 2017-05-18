"""To add:
# Dates with calendar
"""

"""INIT"""

import shelve, os, calendar, time
shelf_file = shelve.open("data")
shelf_file.setdefault("count", 1)


"""GLOBALS"""

penthouse = {"available": 1, "price": 1000, "adults": 25}
luxury = {"available": 5, "price":250, "adults":5, "children":5}
standard_single = {"available": 5, "price": 50, "adults": 1, "children": 0}
twin_single = {"available": 5, "price": 75, "adults": 2, "children": 2}
standard_double = {"available": 5, "price": 99, "adults": 2, "children": 0}
twin_double = {"available": 5, "price": 99, "adults": 2, "children": 2}


"""CLASSES"""

class Guest(object):

    def __init__(self, first_name, second_name, adults, children, nights):
        self.first_name = first_name
        self.second_name = second_name
        self.adults = adults
        self.children = children
        self.nights = nights
        self.deposit = 200
        self.balance = 0

    def check_in(self): # set dates

        check_in_date = input("Enter check in date (DD/MM/YYYY): ")


    def check_out(self):
        pass


"""METHODS"""

def display_available_rooms(called_from=""):
    os.system("cls")

    print("Available rooms: \n{}\n{}\n{}\n{}\n{}\n{}\n".format(
        "[P] Penthouse: " + str(penthouse["available"]),
        "[L] Luxury: " + str(luxury["available"]),
        "[SS] Standard single: " + str(standard_single["available"]),
        "[TS] Twin single: " + str(twin_single["available"]),
        "[SD] Standard double: " + str(standard_double["available"]),
        "[TD] Twin double: " + str(twin_double["available"]),
    ))
    input("Press any key to continue.. ")

    if called_from == "menu":
        menu()
    else:
        return


def get_guest_details(): #with input validation
    os.system("cls")

    first_name = ""
    while not first_name.strip().isalpha():
        first_name = input("Enter first name: ")

    second_name = ""
    while not second_name.strip().isalpha():
        second_name = input("Enter second name: ")

    adults = ""
    while not adults.isdigit():
        adults = input("Enter number of adults: ")

    children = ""
    while not children.isdigit():
        children = input("Enter number of children: ")

    nights = ""
    while not nights.isdigit():
        nights = input("Enter number of nights: ")


    # Create new guest, print details and create new class instance
    shelf_file["count"] += 1
    guest_id = "ID: Guest" + str(shelf_file["count"])

    print("\n" + guest_id +
          "\nFirst: " + first_name +
          "\nSecond: " + second_name +
          "\nAdults: " + adults +
          "\nChildren: " + children +
          "\nNights: " + nights + "\n")

    confirm = ""
    while confirm not in ["Y","N"]:
        confirm = input("Please confirm guest details are correct Y/N: ")
        if confirm.upper() == "Y":
            guest_data = open("guest_data.txt", "a")
            guest_data.write(guest_id + ", " + first_name + ", " + second_name + ", "
                             + adults + ", " + children + ", " + nights + "\n")
            guest_data.close()
            guest_id = Guest(first_name, second_name, adults, children, nights)

            display_available_rooms()
            guest_id.check_in()



        elif confirm.upper() == "N":
            print("Cancelled.. exiting to main menu.. ")
            time.sleep(2)
            menu()
    



def menu():    #Display menu
    os.system("cls")
    print(" 1 : View available rooms")
    print(" 2 : Check in guests")
    print(" 3 : View current guests")
    print(" 4 : Check out guests")
    print(" 5 : Exit program")

    while True:
        menu_item = input("Enter number: ") 

        if menu_item == "1":      
            display_available_rooms("menu")
            
        elif menu_item == "2":    
            get_guest_details()

        elif menu_item == "3":
            os.system("cls")
            break

        elif menu_item == "4":
            os.system("cls")
            break

        elif menu_item == "5":
            shelf_file.close()

            break


"""MAIN"""

menu()