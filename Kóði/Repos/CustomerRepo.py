from Models.Customer import Customer
import os
import csv
clear = lambda: os.system('cls')

class CustomerRepo:
    def __init__(self):
        self.__customers = []

    def add_customer(self, customer):
        # first add to file then to private list
        with open("./Data/customers.csv", "a+", encoding = "utf-8") as customer_file:
            name = customer.get_name()
            soc_sec_num = customer.get_soc_sec_num()
            home_address = customer.get_home_address()
            local_address = customer.get_local_address()
            phone_num = customer.get_phone_num()
            email = customer.get_email()
            driv_license = customer.get_driv_license()
            card_num = customer.get_card_num()
            customer_file.write("{},{},{},{},{},{},{},{}\n".format(name, soc_sec_num, 
                home_address, local_address, phone_num, email, driv_license, card_num))

    def get_customer_list(self):
        if self.__customers == []:
            with open("./Data/customers.csv", "r", encoding = "utf-8") as customer_file:
                customer_reader = csv.reader(customer_file)
                for line in customer_reader:
                    name = line[0]
                    soc_sec_num = line[1]
                    home_address = line[2]
                    local_address = line[3]
                    phone_num = line[4]
                    email = line[5]
                    driv_license = line[6]
                    card_num = line[7]
                    new_customer = Customer(name, soc_sec_num, home_address, local_address, phone_num, email, 
                        driv_license, card_num)
                    self.__customers.append(new_customer)    
        return self.__customers

    def search_by_name(self, name):
        return_list = []
        all_customers = self.get_customer_list()
        for customer in all_customers:
            if customer[0] == name:
                return_list.append(customer)
        return return_list
    
    def search_by_ssn(self, soc_sec_num):
        all_customers = self.get_customer_list()
        for customer in all_customers:
            if customer.get_soc_sec_num() == soc_sec_num:
                return customer
        _ = input("Customer is not in the database.\nPress Enter to continue...")
        return None

    def delete_customer(self, soc_sec_num):
        all_customers = self.get_customer_list()
        for index, customer in enumerate(all_customers):
            if customer[1] == soc_sec_num:
                all_customers.pop(index)
        with open("./Data/customers.csv", "w") as f:
            for customer in all_customers:
                f.write(customer)

    def change_customer(self, soc_sec_num):
        all_customers = self.get_customer_list()
        for customer in all_customers:
            if customer[1]  == soc_sec_num:
                edit_customer = customer[1]
                print(edit_customer)
                print("1. Edit Name\n2. Edit Home Address\n3. Edit Local Address\n"
                    "4. Edit Phone Number\n5. Edit Email\n6. Edit Driver's License\n"
                    "7. Edit Credit/Debit Card Number\n8. Quit") 
                while True:   
                    choice = input("What do you want to change:")
                    if (choice < 1) or (choice > 8):
                        print("Invalid Input\nPress Enter to continue...")
                        clear()
                    else:
                        break
                while True:
                    if choice == 1:
                        print("Current Name: {}".format(edit_customer.get_name()))
                        new_name = input("New Name: ")
                        edit_customer.set_name(new_name)
                        print("New Current Name: {}".format(edit_customer.get_name()))
                    if choice == 2:
                        print("Current Home Address: {}".format(edit_customer.get_home_address()))
                        new_address = input("New Home Address: ")
                        edit_customer.set_home_address(new_address)
                        print("New Current Home Address: {}".format(edit_customer.get_home_address()))
                    if choice == 3:
                        print("Current Local Address: {}".format(edit_customer.get_local_address()))
                        new_local_address = input("New Local Address: ")
                        edit_customer.set_local_address(new_local_address)
                        print("New Current Local Address: {}".format(edit_customer.get_local_address()))
                    if choice == 4:
                        print("Current Phone Number: {}".format(edit_customer.get_phone_num()))
                        new_phone_number = input("New Phone Number: ")
                        edit_customer.set_phone_num(new_phone_number)
                        print("New Current Phone Number: {}".format(edit_customer.get_phone_num()))
                    if choice == 5:
                        print("Current Email: {}".format(edit_customer.get_email()))
                        new_email = input("New Email: ")
                        edit_customer.set_email(new_email)
                        print("New Current Email: {}".format(edit_customer.get_email()))
                    if choice == 6:
                        print("Current Driver's License: {}".format(edit_customer.get_driv_license()))
                        new_driv_license = input("New Driver's License: ")
                        edit_customer.set_driv_license(new_driv_license)
                        print("New Current Driver's License: {}".format(edit_customer.get_driv_license()))
                    if choice == 7:
                        print("Current Credit/Debit Card Number: {}".format(edit_customer.get_card_num()))
                        new_card_num = input("New Credit/Debit Card Number: ")
                        edit_customer.set_card_num(new_card_num)
                        print("New Current Credit/Debit Card Number: {}".format(edit_customer.get_card_num()))
                    if choice == 8:
                        break

    def __str__(self):
        string = "{:<30}{:<25}{:<15}{:<15}{:<15}{:<30}{:<20}{:<30}\n".format("Name:", "Social Security Number:", 
            "Home Address:", "Local Address:", "Phone Number:" , "Email:", "Driver's License:", "Card Number:")
        customerlist = self.get_customer_list()
        for customer in customerlist:
            string += str(customer) + "\n"
        return string