
"""INIT"""
import shelve, os
shelf_file = shelve.open("data")
shelf_file.setdefault("count", 1)
print(shelf_file["count"])


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
        pass

    def check_out(self):
        pass



"""METHODS"""

def interface():    #Display menu
    os.system("cls")
    print(" 1 : View available rooms")
    print(" 2 : Check in guests")
    print(" 3 : View current guests")
    print(" 4 : Check out guests")
    print(" 5 : Exit program")

    while True:
        get_num = input("Enter number: ") # get menu selection

        if get_num == "1":      #Display room availability
            os.system("cls")
            print("Available rooms: \n{}\n{}\n{}\n{}\n{}\n{}".format(
                "Penthouse: " + str(penthouse["available"]),
                "Luxury: " + str(luxury["available"]),
                "Standard single: " + str(standard_single["available"]),
                "Standard twin single: " + str(standard_twin_single["available"]),
                "Standard double: " + str(standard_double["available"]),
                "Standard twin double: " + str(standard_twin_double["available"]),
            ))
            input("Press any key to continue.. ")
            interface()


        elif get_num == "2":    # Get guest details
            first_name = input("Enter guests first name: ")
            second_name = input("Enter guests second name: ")
            adults = input("Enter number of adults: ")
            children = input("Enter number of children: ")

            #Create new guest, print details and create new class instance
            shelf_file["count"] += 1
            guest_id = "guest" + str(shelf_file["count"])
            print(guest_id +
                   "\nFirst name: " + first_name +
                   "\nSecond name: " + second_name +
                   "\nAdults: " + adults +
                   "\nChildren: " + children + "\n")

            guest_id = Guest(first_name, second_name, adults, children)

            print()
            interface()
            break

        elif get_num == "3":
            os.system("cls")

            break

        elif get_num == "4":
            os.system("cls")
            break

        elif get_num == "5":
            shelf_file.close()
            break


"""MAIN"""

interface()