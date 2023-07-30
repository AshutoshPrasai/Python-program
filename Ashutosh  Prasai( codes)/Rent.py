from Costume import get_dictionary, get_file, set_file, print_costumes
from datetime import datetime

def rent_costume():
    user_rented_costumes = []
    costume_dict = get_dictionary(get_file())
    continue_rent = True

    while continue_rent == True:
        item_found = False
        print_costumes()

        while True:
            
            try:
                user_sn = int(input("Enter Costume sn no: "))
                break
            except:
                print("Invalid Costume SN . Please enter again")

        for costume_sn, costume_info in costume_dict.items():
            
            if user_sn == costume_sn:                
                while True:
                    try:
                        user_qty = int(input("Enter Costume quantity"))
                        break
                    except:
                        print("Invalid Costume SN . Please enter again")
                
                if user_qty <= 0 or user_qty > int(costume_info[3]):
                    print("Invalid or insufficient quantity")
                
                else:
                    item_found = True
                    costume_info[3] = str(int(costume_info[3]) - user_qty)
                    user_rented_costumes.append([costume_info, user_qty])
                    set_file(costume_dict)
                    print("Rent successful")
            
        if item_found == False:
            print("Invalid Costume SN")
    
        user_continue_rent = input("Rent more(Y/N)")

        if user_continue_rent.lower() == "n":
            continue_rent = False
            if len(user_rented_costumes) == 0:
                print("Invoice not generated.")
            else:
                user_name = input("Enter your name: ")
                user_contact = input("Enter your email: ")
                create_invoice(user_rented_costumes,user_name, user_contact)


def create_invoice(user_returned_costumes, user_name,user_contact):
    file_name = user_name + "-" + get_datetime() + "-" + "rent_invoice.txt"
    invoice = open(file_name,"w")
    costume_total = 0
    grand_total = 0
    invoice.write("Customer Name: " + user_name)
    invoice.write("\nCustomer Mail: " + user_contact)
    invoice.write("")
    invoice.write("\n| " + "COSTUME NAME|"+ "\t\t\t" + "| BRAND |" +"\t\t"+"| PRICE |" + "| QUANTITY | "  + "| AMOUNT |\n")
    for c in user_returned_costumes:
        price = float(c[0][2].strip("$"))
        costume_total = price * c[1]
        grand_total = grand_total + costume_total
        c[0].pop(-1)
        c[0].append(str(c[1]))
        c[0].append(str(costume_total))
        costume_info = c[0]
        invoice.write(" | ".join(costume_info) + "\n")

    invoice.write("\nGrand Total: " + str(grand_total))
    invoice.close()

    print_invoice(file_name)


def print_invoice(invoice_name):
    invoice_file = open(invoice_name, "r")
    data = invoice_file.readlines()
    print("\n\n Invoice File \n")

    for line in data:
        print(line, end="")

    print("\n\n")
    invoice_file.close()


def get_datetime():
    now = datetime.now()

    now_day = str(now.day)
    now_month = str(now.month)
    now_year = str(now.year)
    now_second = str(now.second)
    now_minute = str(now.minute)
    now_hour = str(now.hour)

    return str(now_hour + "_" + now_minute + "_" + now_second + "_" + now_year + "_" + now_month + "_" + now_day)

