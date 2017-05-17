import shelve, sys
shelf_file = shelve.open("data")
shelf_file.setdefault("count", 1)
print(shelf_file["count"])

class Guest(object):

    def __init__(self, first_name, second_name, adults, children, deposit=200):
        self.first_name = first_name
        self.second_name = second_name
        self.adults = adults
        self.children = children

    def room(self):
        pass

class Rooms(object)



def interface():

    print("1: View available rooms")
    print("2: Check in guests")
    print("3: View current guests")
    print("4: Check out guests")
    print("5: Exit program")

    while True:
        get_num = input("Enter number: ")

        if get_num == "1":

            break

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

            interface()
            break

        elif get_num == "3":


            break

        elif get_num == "4":
            #checkOut()
            break

        elif get_num == "5":
            shelf_file.close()
            break


interface()