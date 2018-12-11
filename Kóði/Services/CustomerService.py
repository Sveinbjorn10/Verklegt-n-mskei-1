from Repos.CustomerRepo import CustomerRepo
from Models.Customer import Customer
import os


clear = lambda: os.system('cls')

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def print_customer_database(self):
        print(self.__customer_repo)

    def customer_info(self):
        additional_driver = []
        
        clear()
        existing = input("Existing customer(Y/N): ").upper()
        if existing == "Y":
            pass
        else:
            print("Fill in the following (*required):")
            first_name = input("\t*First Name: ")
            last_name = input("\t*Last Name: ")
            name = "{} {}".format(first_name, last_name)
            ssn = input("\t*Social Security Number: ")
            home_address = input("\t*Home Address: ")
            local_address = input("\t*Local Address: ")
            mobile_phone = input("\t*Mobile Phone: ")
            email = input("\t*Email: ")
            drivers_license = input("\t*Drivers License: ")
            card_num = input("\t*Credit Card Number: ") #Búið að breyta í required þarf kannski að laga ehv...
            home_phone = input("\tHome Phone: ") #Vantar þetta í customer klasann
            local_phone = input("\tLocal Phone: ") #Vantar þetta í customer klasann
            company_name = input("\tCompany Name: ") #Vantar þetta í customer klasann
            customer = Customer(name, ssn, home_address, local_address, mobile_phone, email, drivers_license, card_num)
            self.__customer_repo.add_customer(customer)

            print("Additional Driver")
            add_first_name = input("\tFirst Name: ")
            additional_driver.append(add_first_name)
            add_last_name = input("\tLast Name: ")
            additional_driver.append(add_last_name)
            add_ssn = input("\tSocial Security Number: ")
            additional_driver.append(add_ssn)
            add_drivers_license = input("\tDrivers License: ")
            additional_driver.append(add_drivers_license)
            clear()
            return customer, additional_driver