from functools import reduce

def isValid(card_num):    #Use the Luhn algorithm to check if card number is valid

    #Store card number as list with list comprehension
    num_list = [num for num in card_num.replace(" ", "")]

    #Starting with the first digit, multiply every second digit by 2
    for i in range(0, 15, 2):
        num_list[i] = int(num_list[i]) * 2

        #Everytime you have a two digit number, add those digits together
        if num_list[i] > 10:
            num_list[i] = (num_list[i] % 10) + 1

    #Sum of all numbers
    result = 0
    for i in num_list:
        result += int(i)

    #Check to see if result is multiple of 10
    if result % 10 == 0:
        print("Card number is valid")
    else:
        print("Invalid card number")


def issuerID(card_num):     #Find card issuer from Issuer Identification Number

    if int(card_num[:2]) >= 51 and int(card_num[:2]) <= 55:
        print("Card issuer is MasterCard")

    if int(card_num[0]) == 4:
        print("Card issuer is Visa")

    if int(card_num[:2]) == 34 or int(card_num[:2]) == 37:
        print("Card issuer is American Express")


#Call functions
isValid("4578 4230 1376 9219")
issuerID("4578 4230 1376 9219")