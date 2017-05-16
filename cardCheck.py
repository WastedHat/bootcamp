from functools import reduce

def isValid(card_num):    #Use the Luhn algorithm to check if card number is valid

    #Store card number as list with list comprehension
    numList = [num for num in card_num.replace(" ", "")]

    #Starting with the first digit, multiply every second digit by 2
    for i in range(0, 15, 2):
        numList[i] = int(numList[i]) * 2

        #Everytime you have a two digit number, add those digits together
        if numList[i] > 10:
            numList[i] = (numList[i] % 10) + 1

    #Sum of all numbers
    result = 0
    for i in numList:
        result += int(i)

    #Check to see if result is multiple of 10
    if result % 10 == 0:
        print("Card number is valid")
    else:
        print("Invalid card number")

    print(result)


isValid("4578 4230 1376 9219")