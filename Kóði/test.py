from Services.CarService import CarService
from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from datetime import datetime
import os

os.system('mode con: cols=190 lines=40')
clear = lambda: os.system('cls')  
            
            
    def confirm_customer(customer):
        print("{:<30}{:<25}{:<15}{:<15}{:<15}{:<30}{:<20}{:<30}".format("Name:", "Social Security Number:", "Home Address:", "Local Address:", "Phone Number:" , "Email:", "Driver's License:", "Card Number:"))
        print(temp_customer)
        confirm = input("Confirm(Y/N): ").upper()
        if confirm == "Y":
            return True
        else:
            return False

    def customer_info(self):        
        while True:
            clear()
            ssn = input("Enter Social Security Number: ")
            temp_customer = self.__customer_repo.search_by_ssn(ssn)
            if temp_customer != None:
                confirm = confirm_customer(temp_customer)
                if confirm:
                    customer = temp_customer
                    break
            else:
                print("Customer not in the system\nPlease fill in the following information:")
                first_name = input("\tFirst Name: ")
                last_name = input("\tLast Name: ")
                name = "{} {}".format(first_name, last_name)

                home_address = input("\tHome Address: ")
                local_address = input("\tLocal Address: ")
                mobile_phone = input("\tMobile Phone: ") 
                email = input("\tEmail: ") 
                drivers_license = input("\tDrivers License: ") 
                card_num = input("\tCredit Card Number: ") 

                customer = Customer(name, ssn, home_address, local_address, mobile_phone, email, drivers_license, card_num)
                self.__customer_repo.add_customer(customer)
                break
        additional_driver = self.get_additional_driver()
        return customer, additional_driver
        
        
        
        
        
        
        while True:
            clear()
            existing = input("Existing customer(Y/N): ").upper()
            if existing == "Y":
                    ssn = input("Enter Social Security Number: ")
                    customer = self.__customer_repo.search_by_ssn(ssn)
                    if customer != None:
                        break            
            else:
                print("Fill in the following:")
                first_name = input("\tFirst Name: ")
                last_name = input("\tLast Name: ")
                name = "{} {}".format(first_name, last_name)
                
                ssn = input("\tSocial Security Number: ")
                if (self.__customer_repo.search_by_ssn(ssn)) != None:
                    print("Customer already exists.")
                    

                home_address = input("\tHome Address: ")
                local_address = input("\tLocal Address: ")
                mobile_phone = input("\tMobile Phone: ") #
                email = input("\tEmail: ") #
                drivers_license = input("\tDrivers License: ") #
                card_num = input("\tCredit Card Number: ") #
                customer = Customer(name, ssn, home_address, local_address, mobile_phone, email, drivers_license, card_num)
                self.__customer_repo.add_customer(customer)
                break

        additional_driver = self.get_additional_driver()
        clear()
        return customer, additional_driver
