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
                search_critera = self.__rental_service.pick_search_criteria(start_date, return_date)
                if search_critera == "1":
                    while True:
                        license_plate = input("Enter Car ID: ")
                        car = self.__car_service.search_by_license_plate(license_plate)
                        if car == None:
                            clear()
                            try_search = input("Search cars(Y/N)?").upper()
                            if try_search == "Y":
                                clear()
                                search_critera = "2"
                                break
                            else:
                                clear()
                                go_back = input("Re-Enter Car ID(Y/N)?").upper()
                                if go_back != "Y":
                                    clear()
                                    search_critera = "3"
                                    break  
                        else:
                            clear()
                            print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}".format("License:", "Make:", "Model:", "Car Class:", "Manuf. Year:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:"))
                            print(car)
                            confirm = input("Confirm car(Y/N)?").upper()
                            if confirm == "Y":
                                clear()
                                break
                            go_back = input("Re-Enter Car ID(Y/N)?").upper()
                            if go_back != "Y":
                                clear()
                                search_critera = "3"
                                break  

                if search_critera == "2":
                    available_cars = self.__car_service.car_by_class(start_date, return_date)
                    if available_cars != None:
                        car = self.__car_service.select_car(available_cars)
                    else:
                        search_critera = "3"
                        clear()
                    # choice = self.__rental_service.search_car(start_date, return_date)
                    # car = self.__rental_service.select_car(choice)
                
                if search_critera != "3":
                    customer, additional_driver = self.__customer_service.customer_info()
                    insurance_list = self.__rental_service.insurance()
                    payment = self.__rental_service.payment()
                    self.__rental_service.print_order_confirmation(customer, car, insurance_list, payment, start_date, return_date, additional_driver)
            if action == "5":
                clear()
                self.__customer_service.print_customer_database()
            if action == "6":
                clear()
                self.__car_service.print_car_database()
                    
                            
