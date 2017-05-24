"""To add:
# Dates with calendar
"""

"""INIT"""

import shelve, os, calendar, time
guest_data = shelve.open("var_data") # persistence via shelve, upgrade to database later.
room_data = shelve.open("var_room")

"""GLOBALS"""

guest_data.setdefault("count", 10000)

# using shelve file to store room data but unable to setdefault() in nested dictionary values
room_data["P"] = {"type": "Penthouse", "available": 1, "price": 1000, "adults": 25}
room_data["L"] = {"type": "Luxury", "available": 5, "price": 250, "adults": 5, "children":5}
room_data["SS"] = {"type": "Standard Single", "available": 5, "price": 50, "adults": 1, "children": 0}
room_data["TS"] = {"type": "Twin Single", "available": 5, "price": 75, "adults": 2, "children": 2}
room_data["SD"] = {"type": "Standard Double", "available": 5, "price": 99, "adults": 2, "children": 0}
room_data["TD"] = {"type": "Twin Double", "available": 5, "price": 99, "adults": 2, "children": 2}



"""METHODS"""

def display_available_rooms(called_from=""):
    os.system("cls")

    print("Available rooms: \n{}\n{}\n{}\n{}\n{}\n{}\n".format(
        "[P]  Penthouse: " + str(room_data["P"]["available"]),
        "[L]  Luxury: " + str(room_data["L"]["available"]),
        "[SS] Standard single: " + str(room_data["SS"]["available"]),
        "[TS] Twin single: " + str(room_data["TS"]["available"]),
        "[SD] Standard double: " + str(room_data["SD"]["available"]),
        "[TD] Twin double: " + str(room_data["TD"]["available"]),
    ))

    if called_from == "menu":
        input("Press any key to return to menu..")
        menu()
    else:
        return


def check_room_availability(room=""): # extend to take in date and nights

    if room == "":
        return False
    elif room_data[room]["available"] <= 0:
        print("No " + room_data[room]["type"] + " rooms available.")
        return False
    else:
        room_data[room]["available"] -= 1


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

    check_in_date = ""
    while not check_in_date:
        check_in_date = input("Enter check in date (DD/MM/YY): ")

    nights = ""
    while not nights.isdigit():
        nights = input("Enter number of nights: ")


    room = ""
    display_available_rooms()
    while room not in ["P", "L", "SS", "TS", "SD", "TD"]:
        try:
            room = input("Enter room: ").upper()

            if check_room_availability(room) == False:
                room = ""
                continue
            else:
                break

        except:
            print('You must enter "P", "L", "SS", "TS", "SD", "TD"')


    store_guest_to_database(first_name, second_name, adults, children, check_in_date, nights, room)


def store_guest_to_database(first_name, second_name, adults, children, check_in_date, nights, room):

    # create guest ID
    os.system("cls")
    guest_data["count"] += 1
    guest_id = "GuestID: " + str(guest_data["count"])[1:]


    guest_data[guest_id] = {"first_name": first_name, "second_name": second_name,
                            "adults": adults, "children": children,
                            "check_in_date": check_in_date, "nights": nights,
                            "room": room}

    view_guest_details(guest_id)

    confirm = ""
    while confirm not in ["Y", "N"]:
        confirm = input("\nPlease confirm guest details are correct Y/N: ")

        if confirm.upper() == "Y":
            print(guest_id + " " + first_name + " " + second_name + " saved to database.")
            input()
            menu()

        elif confirm.upper() == "N":
            del guest_data[guest_id]
            print("Cancelled.. exiting to main menu.. ")
            time.sleep(2)
            menu()


def view_guest_details(guest_id):

    print("\n" + guest_id +
          "\nFirst: " + guest_data[guest_id]["first_name"] +
          "\nSecond: " + guest_data[guest_id]["second_name"] +
          "\nAdults: " + guest_data[guest_id]["adults"] +
          "\nChildren: " + guest_data[guest_id]["children"] +
          "\nIn Date: " + guest_data[guest_id]["check_in_date"] +
          "\nNights: " + guest_data[guest_id]["nights"] +
          "\nRoom: " + str(room_data[guest_data[guest_id]["room"]]["type"]))
            #Access room_data with key from guest_data[guest_id]["room"]

def check_out_guests():
    os.system("cls")

    for guest_id in guest_data.keys():  # BUGFIX: ignore guest_data "count" variable
        if str(guest_data[guest_id]).isdigit():
            continue
        else:
            view_guest_details(guest_id)

    #guest_to_check_out = input("\nEnter the GuestID of guest to check out: ")
    os.system("cls")

    print("Are you sure you want to check out:\n" + view_guest_details("GuestID: 0001"))
    input()


def menu():    #Display menu
    os.system("cls")
    #print(calendar.calendar(17))
    print(" 1 : View available rooms")
    print(" 2 : Check in guests")
    print(" 3 : View guest details")
    print(" 4 : Check out guests")
    print(" 5 : Exit program")

    while True:
        menu_item = input("Enter number: ") 

        if menu_item == "1":      
            display_available_rooms("menu")
            
        elif menu_item == "2":    
            get_guest_details()

        elif menu_item == "3": # View all guest details

            for guest_id in guest_data.keys(): #BUGFIX: ignore guest_data "count" variable
                if str(guest_data[guest_id]).isdigit():
                    continue
                else:
                    view_guest_details(guest_id)
            input("\nPress any key to return to menu..")
            menu()


        elif menu_item == "4":
            check_out_guests()

        elif menu_item == "5": # TOFIX: this option rreturns to menu
            guest_data.close()

            break


"""MAIN"""
menu()