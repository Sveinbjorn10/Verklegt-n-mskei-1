from Services.CarService import CarService
from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from datetime import datetime
import os

clear = lambda: os.system('cls')

class Employee:

    def __init__(self):
        pass
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        self.__rental_service = RentalService()

    def main_screen(self):
        action = ""
        while (action != "8"):
            print("Welcome to HSST Rental Software")
            print("\t1. Rent a car")
            print("\t2. Return a car")
            print("\t3. Available cars")
            print("\t4. Price list")
            print("\t5. Customer database")
            print("\t6. Car database")
            print("\t7. Rental database")
            print("\t8. Exit")
            action = input("Input choice here: ")

            if action == "1":
                clear()
                start_date, return_date = self.__rental_service.pick_date()
                search_critera = self.__rental_service.pick_search_criteria(start_date, return_date)
                if search_critera == "1":
                    pass
                if search_critera == "2":
                    choice = self.__rental_service.search_car(start_date, return_date)

            if action == "5":
                clear()
                self.__customer_service.print_customer_database()
            if action == "6":
                clear()
                self.__car_service.print_car_database()
                    
                            