from Services.CarService import CarService
from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from datetime import datetime
import os

os.system('mode con: cols=190 lines=40')
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
                while True:
                    clear()
                    search_critera = self.__rental_service.pick_search_criteria(start_date, return_date)
                    if search_critera == "1":
                            car = self.__car_service.search_by_license_plate()
                            if car != None:
                                    break
                    
                    if search_critera == "2":
                        available_cars = self.__car_service.car_by_class(start_date, return_date)
                        if available_cars != None:
                            if available_cars != []:
                                car = self.__car_service.select_car(available_cars)
                                break
                            else:
                                _ = input("No car available in that class.\nPress Enter to continue...")
                        else:
                            clear()
                    if search_critera == "3":
                        break
                    
                if search_critera in ["1", "2"]:
                    customer, additional_driver = self.__customer_service.customer_info()
                    while True:
                        insurance_list = self.__rental_service.insurance()
                        payment = self.__rental_service.payment()
                        if payment != None:
                            break
                    self.__rental_service.print_order_confirmation(customer, car, insurance_list, payment, start_date, return_date, additional_driver)
                    clear()
            if action == "3":
                clear()
                self.__car_service.get_available_cars_database(self.__car_service.get_available_cars())
            if action == "5":
                clear()
                self.__customer_service.print_customer_database_menu()
                choice = int(input("Input Choice Here: "))
                while (choice < 1) or (choice > 5):
                    print("Incorrect Input")
                    choice = input("Input Choice Here: ")
                if choice == 1:
                    clear()
                    self.__customer_service.print_customer_database()
                    _ = input("Press Enter To Return To Main Menu...")
                if choice == 2:
                    self.__customer_service.customer_info()
                if choice == 3:
                    ssn = input("Input SSN For Customer To Update: ")
                    self.__customer_service.change_customer(ssn)
                if choice == 4:
                    ssn = input("Input SSN For Customer To Delete: ")
                    self.__customer_service.delete_customer(ssn)
                else:
                    clear()
            if action == "6":
                clear()
                self.__car_service.print_car_database_menu()
                choice = int(input("Input Choice Here: "))
                while (choice < 1) or (choice > 5):
                    print("Incorrect Input")
                    choice = input("Input Choice Here: ")
                if choice == 1:
                    clear()
                    self.__car_service.print_car_database()
                    _ = input("Press Enter To Return To Main Menu...")
                if choice == 2:
                    self.__car_service.car_info()
                if choice == 3:
                    car_id = input("Input Car License To Update: ")
                    self.__car_service.update_car_info(car_id)
                if choice == 4:
                    car_id = input("Input Car License To Delete: ")
                    self.__car_service.delete_car(car_id)
                else:
                    clear()
            if action == "7":
                clear()
                self.__rental_service.print_rental_database()
                _ = input("Press Enter To Return To Main Menu...")
                clear()