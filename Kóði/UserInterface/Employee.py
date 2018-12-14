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

            if action == "1": #Rent A Car
                clear()
                start_date, return_date = self.__rental_service.pick_date()
                while True:
                    clear()
                    search_critera = self.__rental_service.pick_search_criteria_rent(start_date, return_date)
                    if search_critera == "1":
                        car = self.__car_service.search_by_car_id()
                        if car.get_availability() == "No":
                            clear()
                            _ = input("Car not available.\nPress Enter to continue...")
                        else:
                            if car != None:
                                break
                    
                    if search_critera == "2":
                        available_cars = self.__car_service.car_by_class(start_date, return_date) #laga ehv hér
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
                    customer, additional_driver = self.__customer_service.customer_info(False)
                    while True:
                        insurance_list = self.__rental_service.insurance()
                        payment = self.__rental_service.payment()
                        if payment != None:
                            break
                    self.__rental_service.print_order_confirmation(customer, car, insurance_list, payment, start_date, return_date, additional_driver)
                    clear()

            if action == "2": #Return A Car
                clear()
                frue = False
                while True:
                    search_criteria = self.__rental_service.pick_search_criteria_return()
                    clear()
                    if search_criteria == "1":
                        car = self.__car_service.search_by_car_id()
                        clear()
                        if car != None:
                            rental = self.__rental_service.get_open_rental_for_car(car)
                            if rental != None:
                                customer = self.__customer_service.get_customer_for_rental(rental.get_ssn())
                                frue = True
                            else:
                                _ = input("No open rental for {}.\nPress Enter to continue...".format(car.get_car_id()))
                                clear()
                    if search_criteria == "2":
                        while True:
                            while True: #Þetta shit er til ehvstaðar annarsstaðar
                                print("Customer information:")
                                ssn = input("\tEnter Social Security Number: ")
                                trulse = True
                                for num in ssn:
                                    try:
                                        int(num)
                                    except:
                                        trulse = False

                                if (len(ssn) == 10) and (trulse == True):
                                    
                                    break
                                else:
                                    _ = input("Please enter a valid Social Security Number\nPress Enter to continue...")
                                clear()
                            temp_customer = self.__customer_service.search_by_ssn(ssn, False)
                            if temp_customer != None:
                                clear()
                                confirm = self.__customer_service.confirm_customer(temp_customer)
                            else:
                                confirm = False
                                clear()
                                break
                            if confirm == True:
                                customer = temp_customer
                                clear()
                                rental = self.__rental_service.get_open_rental_for_customer(customer, search_criteria)
                                if rental != None:
                                    car = self.__car_service.get_car_for_rental(rental)
                                    frue = True
                                    break
                                else:
                                    break
                                
                    if search_criteria == "3":
                        break

                    if (search_criteria in ["1", "2"]) and (frue == True):
                        fuel_price, fuel_level = self.__rental_service.fuel_status(car)
                        damage = self.__rental_service.damage_check()
                        clear()
                        self.__rental_service.finish_order(rental, car, customer, [fuel_price, fuel_level], damage)

            if action == "3": #Available Cars 
                clear()
                self.__car_service.get_available_cars_database(self.__car_service.get_available_cars())
                _ = input("Press Enter To Return To Main Menu...")
                clear()
            if action == "4": #Price List
                clear()
                while True:
                    self.__car_service.print_price_options()
                    choice = input("Input Choice Here: ")
                    clear()
                    if choice in ["1", "2", "3"]:
                        break
                    else:
                        _ = input("Invalid input.\nPress Enter to continue...")
                        clear()
                if choice == "1":
                    self.__car_service.print_car_price_list()
                    _ = input("Press Enter To Return To Main Menu...")
                    clear()
                if choice == "2":
                    self.__car_service.print_insurance_price_list()
                    _ = input("Press Enter To Return To Main Menu...")
                    clear()
                else:
                    clear()
            if action == "5": #Customer Database
                clear()
                while True:
                    self.__customer_service.print_customer_database_menu()
                    choice = input("Input Choice Here: ")
                    clear()
                    if choice in ["1", "2", "3", "4", "5", "6"]:
                        break
                    else:
                        _ = input("Invalid input.\nPress Enter to continue...")
                        clear()

                if choice == "1":
                    self.__customer_service.print_customer_database()
                    _ = input("Press Enter To Return To Main Menu...")
                    clear()
                if choice == "2":
                    ssn = input("Input SSN to Search: ")
                    customer = self.__customer_service.search_by_ssn(ssn, False)
                    print(customer)
                    _ = input("Press Enter to continue...")
                    clear()
                if choice == "3":
                    self.__customer_service.customer_info(True)
                    clear()
                if choice == "4":
                    ssn = input("Input SSN For Customer To Update: ")
                    self.__customer_service.change_customer(ssn)
                    clear()
                if choice == "5":
                    ssn = input("Input SSN For Customer To Delete: ")
                    self.__customer_service.delete_customer(ssn)
                    clear()
                else:
                    clear()
            if action == "6": #Car Database
                clear()
                while True:
                    self.__car_service.print_car_database_menu()
                    choice = input("Input Choice Here: ")
                    clear()
                    if choice in ["1", "2", "3", "4", "5", "6"]:
                        break
                    else:
                        _ = input("Invalid input.\nPress Enter to continue...")
                        clear()

                if choice == "1":
                    self.__car_service.print_car_database()
                    _ = input("Press Enter To Return To Main Menu...")
                    clear()
                if choice == "2":
                    while True:
                        self.__car_service.print_search_options()
                        search_criteria = input("Input Search Criteria: ")
                        clear()
                        if search_criteria in ["1", "2", "3", "4"]:
                            break

                    if search_criteria == "1":
                        self.__car_service.search_by_car_id()
                        clear()
                    if search_criteria == "2":
                        self.__car_service.search_by_class()
                        clear()
                    if search_criteria == "3":
                        self.__car_service.search_by_model()
                        clear()
                    else:
                        clear()
                if choice == "3":
                    self.__car_service.car_info()
                    clear()
                if choice == "4":
                    car_id = input("Input Car ID To Update: ").upper()
                    self.__car_service.update_car_info(car_id)
                    clear()
                if choice == "5":
                    car_id = input("Input Car ID To Delete: ")
                    self.__car_service.delete_car(car_id)
                    clear()
                else:
                    clear()
            if action == "7": #Rental Database
                clear()
                self.__rental_service.print_rental_database_menu()
                choice = int(input("Input Choice Here: "))
                while (choice < 1) or (choice > 3):
                    print("Incorrect Input")
                    choice = int(input("Input Choice Here: "))
                if choice == 1:
                    clear()
                    self.__rental_service.print_view_rental_database_menu()
                    search_criteria = int(input("Input Choice Here: "))
                    while (search_criteria < 1) or (search_criteria > 3):
                        print("Incorrect Input")
                        search_criteria = int(input("Input Choice Here: "))
                    if search_criteria == 1:
                        self.__rental_service.print_rental_database()
                        _ = input("Press Enter to continue...")
                    if search_criteria == 2:
                        self.__rental_service.get_open_car_rentals_for_database()
                        _ = input("Press Enter to continue...")
                    else:
                        clear()
                if choice == 2:
                    clear()
                    self.__rental_service.print_search_rental_database_menu()
                    search_criteria = int(input("Input Choice Here: "))
                    while (search_criteria < 1) or (search_criteria > 3):
                        print("Incorrect Input")
                        search_criteria = int(input("Input Choice Here: "))
                    if search_criteria == 1:
                        ssn = input("Input SSN: ")
                        self.__rental_service.search_rentals_by_ssn(ssn)
                        _ = input("Press Enter to continue...")
                    if search_criteria == 2:
                        car_id = input("Input Car ID: ").upper()
                        self.__rental_service.search_by_car_id_rentals(car_id)
                        _ = input("Press Enter to continue...")
                    else:
                        clear()
                if choice == 3:
                    clear()
                clear()
