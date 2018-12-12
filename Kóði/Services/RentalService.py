from Repos.RentalRepo import RentalRepo
from Repos.CarRepo import CarRepo
from Models.Car import Car
from datetime import datetime
import os
import csv

os.system('mode con: cols=190 lines=40')

clear = lambda: os.system('cls')

class RentalService:
    def __init__(self):
        self.__rental_repo = RentalRepo()
        self.__car_repo = CarRepo()

    def print_rental_database(self):
        print(self.__rental_repo)
    
    def pick_date(self):
        while True:
            try:
                date = input("Choose a starting date(DD/MM/YYYY): ")
                date_list = [int(word) for word in date.split("/")]
                start_date = datetime(date_list[2], date_list[1], date_list[0])
                
                date = input("Choose a return date(DD/MM/YYYY): ")
                date_list = [int(word) for word in date.split("/")]
                return_date = datetime(date_list[2], date_list[1], date_list[0])
                correct = True
            except:
                _ = input("Invalid input.\nPress Enter to continue...")
                correct = False
                clear()

            if correct:
                if (return_date > start_date) and (start_date > datetime.today()):
                    clear()
                    break
                else:
                    _ = input("Invalid time period.\nPress Enter to continue...")
                    clear()
        return start_date, return_date

    def print_time_period(self, start, end):
        start_date = "{}/{}/{}".format(start.day, start.month, start.year)
        end_date = "{}/{}/{}".format(end.day, end.month, end.year)
        print("({}) ---> ({})".format(start_date, end_date))

    def pick_search_criteria(self, start, end):
        while True:
            self.print_time_period(start, end)
            print("\t1. Car ID.")
            print("\t2. Search for car.")
            print("\t3. Return to menu.")
            choice = input("Input choice here: ")
            if choice in ["1", "2", "3"]:
                clear()
                return choice
            else:
                _ = input("Invalid input.\nPress Enter to continue...")
                clear()
        
    def search_car(self, start, end):
        while True:
            self.print_time_period(start, end)
            print("Search for car:")
            print("\t1. Small car.")
            print("\t2. Family car.")
            print("\t3. Van.")
            print("\t4. SUV.")
            print("\t5. Every type.")
            print("\t6. Go back.")
            choice = input("Input choice here: ")
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return int(choice)
            else: 
                _ = input("Invalid input.\nPress Enter to continue...")
                clear()

    def print_list(self, my_list):
        print("Available cars")
        print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ","Nr.", "License", "Make", "Model", "Manuf. Year", "Seats", "Doors", "Color", "Transmission", "Fuel", "Price per day"))
        for index, car in enumerate(my_list):
            print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ", (index + 1), car.get_license_plate(), car.get_make(), car.get_model(), car.get_manuf_year(), car.get_seats(), car.get_doors(), car.get_color(), car.get_transmission(), car.get_fuel_type(), car.get_price()))

    def select_car(self, car_class):
        car_list = self.__car_repo.get_car_list()
        # available_cars = [car for car in car_list if ((car[4] == car_class) and (car[-1] == "True"))]
        available_cars = [car for car in car_list if (car.get_availability() == "True") and (car.get_car_class() == car_class)]
        clear()
        while True:
            self.print_list(available_cars)
            try:
                car_choice = int(input("Select a car: "))
                if (car_choice > 0) and (car_choice <= len(available_cars)):
                    
                    return available_cars[car_choice]
                else:
                    _ = input("Invalid input!\nPress Enter to continue...")
                    clear()
            except:
                _ = input("Invalid input!\nPress Enter to continue...")
                clear()

    def insurance(self):
        print("Insurance options:")
        print("\t1. Included Insurance")
        print("\t2. Insurance Package 1")
        print("\t3. Insurance Package 2")
        print("\t4. Return to Customer Info") # Spurning hvort við eigum að gerae þetta...
        os.system("start python insurance.py ")
        choice = int(input("What insurance package do you want? "))
        clear()
        return choice
    
    def payment(self):
        print("Payment methods:")
        print("\t1. Cash.")
        print("\t2. Credit Card")
        print("\t3. Debit Card.")
        print("\t4. Return to Insurance Info.")
        choice = input("Preferred payment method: ")
        clear()
        if choice == "1":
            return "Cash"
        if choice == "2":
            return "Credit Card"
        if choice == "3":
            return "Debit Card"
    
    def get_order_number(self):
        rental_list = []
        date = datetime.today()
        year = str(date.year)
        year[2:]
        with open("Data/rentals.csv", "r", encoding = "utf-8") as rentals:
            csv_reader = csv.reader(rentals)
            for rental in csv_reader:
                rental_list.append(rental)
        order_number = "ON{}-{:0>5}".format(year[2:] ,str((int(rental_list[-1][0][6:]) + 1)))
        return order_number
    
    def get_insurance_info(self, car_class, insurance_num):
            insurance_list = []
            with open("./Data/insurance.csv", "r", encoding = "utf-8") as f:
                    csv_reader = csv.reader(f)
                    for line in csv_reader:
                            insurance_list.append(line)
            insurance_cost =  insurance_list[insurance_num - 1][car_class]
            print(insurance_cost)
            insurance_name = insurance_list[insurance_num - 1][0]
            # insurance_info = [insurance_list[insurance_num - 1][5:]]

            insurance_info = [info for info in insurance_list[insurance_num - 1][5:]]
            return [int(insurance_cost), insurance_name, insurance_info]
        
    def print_order_confirmation(self, customer, car, insurance, payment, 
        start, end, additional_driver = "Empty"):
        delta = end - start
        days = int(delta.days)
        start_date = "{}/{}/{}".format(str(start.day), str(start.month), str(start.year))
        end_date = "{}/{}/{}".format(str(end.day), str(end.month), str(end.year))

        order_number = self.get_order_number()
        name = customer.get_name()
        ssn = customer.get_soc_sec_num()
        home_address = customer.get_home_address()
        email = customer.get_email()
        phone = customer.get_phone_num()

        if additional_driver != "Empty":    
            additional_driver_name = "{} {}".format(additional_driver[0], additional_driver[1])
            additional_driver_ssn = additional_driver[2]
            additional_driver_driv_license = additional_driver[3]

        car_make = car.get_make()
        car_model = car.get_model()
        car_plate = car.get_license_plate()
        car_price_per_day = car.get_price()

        car_price = car_price_per_day * days
        car_price_w_vat = car_price * 1.24
        car_string = "{} {} ({})".format(car_make, car_model, car_plate)
        car_class = car.get_car_class()

        insurance_list = self.get_insurance_info(car_class, insurance)
        insurance_cost_per_day = insurance_list[0]
        insurance_cost = insurance_cost_per_day * days
        insurance_cost_w_vat = insurance_cost * 1.24
        insurance_name = insurance_list[1]
        insurance_info = insurance_list[2]

        total_price = car_price + insurance_cost
        vat = total_price * 0.24
        total_price_w_vat = total_price * 1.24

        print("{:<165}".format(order_number))
        print("{:<165}{:<20}".format(name, "HSST Rental Company"))
        print("{:<165}{:<20}".format(ssn, "SSN: 040499-2059"))
        print("{:<165}{:<20}".format(home_address, "Hvergiland 88"))
        print("{:<165}{:<20}".format(email, "hsst@hsst.is"))
        print("{:<165}{:<20}".format(phone, "Phone: 642-1000"))
        print("\n\n")
        print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Item", "Description", "Start Date", "Return Date", "Price per day",  "Total Price no VAT", "Total Price with VAT"))
        print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Car Rental", car_string, start_date, end_date, str(car_price_per_day) + " kr", str(car_price) + " kr", str(int(car_price_w_vat)) + " kr"))
        print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Insurance", insurance_name, "", "", str(insurance_cost_per_day) + " kr", str(insurance_cost) + " kr", str(int(insurance_cost_w_vat)) + " kr"))
        
        for info in insurance_info:
                print("{:<20}-{:<45}".format("", info))
        print("\n")

        #Additional driver here
        if additional_driver != "Empty": 
            print("{:<20}{:<45}".format("Additional Driver", additional_driver_name))
            print("{:<20}SSN: {:<45}".format("", additional_driver_ssn))
            print("{:<20}Drivers License: {:<45}".format("", additional_driver_driv_license))

        print("\n\n")
        print("{:.<100}{:.>85}".format("Total Price no VAT ", str(int(total_price)) + " kr"))
        print("{:.<100}{:.>85}".format("VAT ", str(int(vat)) + " kr"))
        print("{:.<100}{:.>85}".format("Total Price with VAT ", str(int(total_price_w_vat)) + " kr"))
        print("\n\n")
        print("Payment: {}".format(payment))
        _ = input()