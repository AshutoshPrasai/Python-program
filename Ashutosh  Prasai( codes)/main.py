from Rent import rent_costume
from Return import return_costume

def intro_message():
    print("==================================================");
    print("             WELCOME TO COSTUME RENTAL            ")
    print("==================================================");


def choice_message():
    print("Select the number")
    print("(1) || 1 to rent a costume.")
    print("(2) || 2 to return a costume.")
    print("(3) || 3 to exit.")


def end_message():
    print("End of program")


def main():
    intro_message()

    continue_loop = True

    while continue_loop == True:
        choice_message()
        option = input("Enter a choice:")

        # try:
        option = int(option)
        if option == 1:
            rent_costume()
        elif option == 2:
            return_costume()
        elif option == 3:
            end_message()
            return
        else:
            print("invalid choice")
        # except:
        #     print("Invalid costume SN")
        #     return


main()
