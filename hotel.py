"""To add:
# Dates with calendar
"""

"""INIT"""

import shelve, os, calendar
shelf_file = shelve.open("data")
shelf_file.setdefault("count", 1)
guest_data = open("guest_data.txt","a")


"""GLOBALS"""

penthouse = {"available": 1, "price": 1000, "adults": 25}
luxury = {"available": 25, "price":250, "adults":5, "children":5}
standard_single = {"available": 25, "price": 50, "adults": 1, "children": 0}
standard_twin_single = {"available": 25, "price": 75, "adults": 2, "children": 2}
standard_double = {"available": 25, "price": 99, "adults": 2, "children": 0}
standard_twin_double = {"available": 25, "price": 99, "adults": 2, "children": 2}


"""CLASSES"""

class Guest(object):

    def __init__(self, first_name, second_name, adults, children):
        self.first_name = first_name
        self.second_name = second_name
        self.adults = adults
        self.children = children
        self.deposit = 200
        self.balance = 0

    def check_in(self):

        confirm = input("Are you sure you want to check guest ")

    def check_out(self):
        pass


"""METHODS"""

def display_available_rooms():
    os.system("cls")

    print("Available rooms: \n\n{}\n{}\n\n{}\n{}\n\n{}\n{}\n".format(
        "Penthouse: " + str(penthouse["available"]),
        "Luxury: " + str(luxury["available"]),
        "Standard single: " + str(standard_single["available"]),
        "Standard twin single: " + str(standard_twin_single["available"]),
        "Standard double: " + str(standard_double["available"]),
        "Standard twin double: " + str(standard_twin_double["available"]),
    ))
    input("Press any key to continue.. ")
    menu()


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


    guest_id = Guest(first_name, second_name, adults, children)
    input("Press any key to continue.. ")
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
            display_available_rooms()
            
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