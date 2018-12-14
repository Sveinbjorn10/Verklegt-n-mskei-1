from Repos.CustomerRepo import CustomerRepo
from Models.Customer import Customer
import os


clear = lambda: os.system('cls')

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def print_customer_database(self):
        print(self.__customer_repo)

    def get_customer_for_rental(self, rental_ssn):
        return self.__customer_repo.get_customer_for_rental(rental_ssn)

    def get_additional_driver(self):
        yes_no = input("Additional Driver(Y/N)? ").upper()
        clear()
        if yes_no == "Y":
            additional_driver = []
            clear()
            print("Additional Driver")
            add_first_name = input("\tFirst Name: ")
            additional_driver.append(add_first_name)
            add_last_name = input("\tLast Name: ")
            additional_driver.append(add_last_name)
            add_ssn = input("\tSocial Security Number: ")
            additional_driver.append(add_ssn)
            add_drivers_license = input("\tDriver's License: ")
            additional_driver.append(add_drivers_license)
        else:
            additional_driver = "Empty"

        return additional_driver

    def confirm_customer(self, customer):
        print("{:<30}{:<25}{:<15}{:<15}{:<15}{:<30}{:<20}{:<30}".format("Name:", "Social Security Number:", "Home Address:", "Local Address:", "Phone Number:" , "Email:", "Driver's License:", "Card Number:"))
        print(customer)
        confirm = input("Confirm(Y/N): ").upper()
        if confirm == "Y":
            return True
        else:
            return False

    def customer_info(self, in_database):
        while True:
            clear()
            while True:
                print("Customer information:")
                ssn = input("\tEnter Social Security Number: ")

                try:
                    ssn = int(ssn)
                except:
                    pass
                
                if (len(str(ssn)) == 10) and (type(ssn) == int):
                    break
                else:
                    if in_database == False:
                        _ = input("Please enter a valid Social Security Number\nPress Enter to continue...")
                clear()

            temp_customer = self.__customer_repo.search_by_ssn(ssn, in_database)
            if temp_customer != None:
                clear()
                confirm = self.confirm_customer(temp_customer)
                clear()
                if confirm:
                    customer = temp_customer
                    break
            else:
                clear()
                if in_database == False:
                    try_again = input("Try another Social Security Number(Y/N)?").upper()
                if in_database == True:
                    try_again = "N"
                if try_again != "Y":
                    clear()
                    print("Creating Customer - SSN: {}".format(ssn))
                    print("Please fill in the following information:")
                    first_name = input("\tFirst Name: ")
                    last_name = input("\tLast Name: ")
                    name = "{} {}".format(first_name, last_name)
                    home_address = input("\tHome Address: ")
                    local_address = input("\tLocal Address: ")
                    mobile_phone = input("\tMobile Phone: ") 
                    email = input("\tEmail: ") 
                    drivers_license = input("\tDriver's License: ") 
                    card_num = input("\tCredit Card Number: ") 

                    customer = Customer(name, ssn, home_address, local_address, mobile_phone, email, drivers_license, card_num)
                    self.__customer_repo.add_customer(customer)
                    break
        if in_database == False:
            additional_driver = self.get_additional_driver()
            return customer, additional_driver
        else:
            return customer

    def print_customer_database_menu(self):
        print("\t1. View Customer Database")
        print("\t2. Search Customer")
        print("\t3. Add Customer")
        print("\t4. Edit Customer")
        print("\t5. Delete Customer")
        print("\t6. Return to Main Menu")

    def change_customer(self, ssn):
        return self.__customer_repo.change_customer(ssn)
    
    def delete_customer(self, ssn):
        return self.__customer_repo.delete_customer(ssn)

    def search_by_ssn(self, ssn):
        return self.__customer_repo.search_by_ssn(ssn)


