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
            ssn = customer.get_ssn()
            home_address = customer.get_home_address()
            local_address = customer.get_local_address()
            phone_num = customer.get_phone_num()
            email = customer.get_email()
            driv_license = customer.get_driv_license()
            card_num = customer.get_card_num()
            customer_file.write("{},{},{},{},{},{},{},{}\n".format(name, ssn, 
                home_address, local_address, phone_num, email, driv_license, card_num))

    def get_customer_list(self):
        if self.__customers == []:
            with open("./Data/customers.csv", "r", encoding = "utf-8") as customer_file:
                customer_reader = csv.reader(customer_file)
                for line in customer_reader:
                    name = line[0]
                    ssn = line[1]
                    home_address = line[2]
                    local_address = line[3]
                    phone_num = line[4]
                    email = line[5]
                    driv_license = line[6]
                    card_num = line[7]
                    new_customer = Customer(name, ssn, home_address, local_address, phone_num, email, 
                        driv_license, card_num)
                    self.__customers.append(new_customer)    
        return self.__customers
    
    def search_by_ssn(self, ssn, in_database):
        all_customers = self.get_customer_list()
        for customer in all_customers:
            if customer.get_ssn() == ssn:
                return customer
        if in_database == False:
            _ = input("Customer is not in the database.\nPress Enter to continue...")
        return None

    def delete_customer(self, ssn):
        all_customers = self.get_customer_list()
        for index, customer in enumerate(all_customers):
            if customer.get_ssn() == ssn:
                all_customers.pop(index)
        with open("./Data/customers.csv", "w", encoding = "utf-8") as customer_file:
            customer_file.truncate()
            for customer in all_customers:
                self.add_customer(customer)
        clear()
                

    def change_customer(self, ssn):
        all_customers = self.get_customer_list()
        for customer in all_customers:
            if customer.get_ssn() == ssn:
                edit_customer = customer
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
                        print("Name Changed To: {}".format(edit_customer.get_name()))
                    if choice == 2:
                        print("Current Home Address: {}".format(edit_customer.get_home_address()))
                        new_address = input("New Home Address: ")
                        edit_customer.set_home_address(new_address)
                        print("Home Address Changed To: {}".format(edit_customer.get_home_address()))
                    if choice == 3:
                        print("Current Local Address: {}".format(edit_customer.get_local_address()))
                        new_local_address = input("New Local Address: ")
                        edit_customer.set_local_address(new_local_address)
                        print("Local Address Changed To: {}".format(edit_customer.get_local_address()))
                    if choice == 4:
                        print("Current Phone Number: {}".format(edit_customer.get_phone_num()))
                        new_phone_number = input("New Phone Number: ")
                        edit_customer.set_phone_num(new_phone_number)
                        print("Phone Number Changed To: {}".format(edit_customer.get_phone_num()))
                    if choice == 5:
                        print("Current Email: {}".format(edit_customer.get_email()))
                        new_email = input("New Email: ")
                        edit_customer.set_email(new_email)
                        print("Email Changed To: {}".format(edit_customer.get_email()))
                    if choice == 6:
                        print("Current Driver's License: {}".format(edit_customer.get_driv_license()))
                        new_driv_license = input("New Driver's License: ")
                        edit_customer.set_driv_license(new_driv_license)
                        print("Driver's License Changed To: {}".format(edit_customer.get_driv_license()))
                    if choice == 7:
                        print("Current Credit/Debit Card Number: {}".format(edit_customer.get_card_num()))
                        new_card_num = input("New Credit/Debit Card Number: ")
                        edit_customer.set_card_num(new_card_num)
                        print("Credit/Debit Card Number Changed To: {}".format(edit_customer.get_card_num()))
                    if choice == 8:
                        break

    def get_customer_for_rental(self, rental_ssn):
        customer_list = self.get_customer_list()
        for customer in customer_list:
            if customer.get_ssn() == rental_ssn:
                return customer

    def __str__(self):
        string = "{:<30}{:<30}{:<25}{:<20}{:<15}{:<30}{:<20}{:<30}{:<200}\n".format("Name:", "SSN:", 
            "Home Address:", "Local Address:", "Phone Number:" , "Email:", "Driver's License:", "Card Number:",("-"*200))
        customerlist = self.get_customer_list()
        for customer in customerlist:
            string += str(customer) + "\n"
        return string