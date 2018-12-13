from Repos.RentalRepo import RentalRepo
from Repos.CarRepo import CarRepo
from Models.Car import Car
from Models.Rental import Rental
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
        today = datetime.today()
        now = datetime(today.year, today.month, today.day)
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
                if (return_date > start_date) and (start_date >= now):
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

    def pick_search_criteria_rent(self, start, end):
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
        
    def pick_search_criteria_return(self):
        while True:
            print("1. Car ID.")
            print("2. Customer SSN.")
            print("3. Return to menu.")
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
            print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ", (index + 1), car.get_car_id(), car.get_make(), car.get_model(), car.get_manuf_year(), car.get_seats(), car.get_doors(), car.get_color(), car.get_transmission(), car.get_fuel_type(), car.get_price()))

    def insurance(self):
        while True:
            print("Insurance options:")
            print("\t1. Included Insurance")
            print("\t2. Insurance Package 1")
            print("\t3. Insurance Package 2")
            print("\t4. See Insurance Info again") # Spurning hvort við eigum að gerae þetta...
            os.system("start python insurance.py ")
            try:
                choice = int(input("What insurance package do you want? "))
                if choice in [1, 2, 3]:
                    clear()
                    return choice
            except:
                _ = input("Invalid input.\nPress Enter to continu...")
            clear()

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
        elif choice == "2":
            return "Credit Card"
        elif choice == "3":
            return "Debit Card"
        else:
            return None

    def get_order_number(self):
        rental_list = []
        date = datetime.today()
        year = str(date.year)
        with open("Data/rentals.csv", "r", encoding = "utf-8") as rentals:
            csv_reader = csv.reader(rentals)
            for rental in csv_reader:
                rental_list.append(rental)

        if ((os.stat("Data/Rentals.csv").st_size) == 0) or (rental_list[-1][0][2:4] != (year[2:])):
            order_number = "ON{}-00001".format(year[2:])
        else:
            order_number = "ON{}-{:0>5}".format(year[2:] ,str((int(rental_list[-1][0][6:]) + 1))) 
        return order_number

    def get_insurance_info(self, car_class, insurance_num):
            insurance_list = []
            with open("./Data/insurance.csv", "r", encoding = "utf-8") as f:
                    csv_reader = csv.reader(f)
                    for line in csv_reader:
                            insurance_list.append(line)
            insurance_cost =  insurance_list[int(insurance_num) - 1][car_class]
            insurance_name = insurance_list[int(insurance_num) - 1][0]
            # insurance_info = [insurance_list[insurance_num - 1][5:]]

            insurance_info = [info for info in insurance_list[int(insurance_num) - 1][5:]]
            return [int(insurance_cost), insurance_name, insurance_info]
        
    def print_order_confirmation(self, customer, car, insurance, payment, start, end, additional_driver):
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
        car_plate = car.get_car_id()
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
        confirm = input("Confirm order(Y/N):").upper()
        if confirm == "Y":
            rental = Rental(order_number, name, ssn, car_plate, insurance, start_date, end_date, str(int(total_price_w_vat)), "Open", payment)
            self.__rental_repo.add_rental(rental)
        clear()

<<<<<<< HEAD
    def search_by_car_id_rentals(self, car_id):
        return self.__rental_repo.search_by_car_id(car_id)
=======
    def search_by_license_plate_rentals(self, license_plate): #Hægt að nota fyrir search criteria 2
        return self.__rental_repo.search_by_license_plate_rentals(license_plate)
>>>>>>> 47054d774b6955f197f8ac0ffd4a2ce39037367c

    def open_rentals(self, rental_list):
        open_rentals = []
        for rental in rental_list:
            if rental.get_status() == "Open":
                open_rentals.append(rental)
        return open_rentals

    def print_open_rentals(self, open_rentals, search_criteria):
        print("{:<15}{:<30}{:<12}{:<15}{:<20}{:<12}{:<12}{:<20}{:<5}".format("Order Number", "Name", "SSN", "License Plate", "Insurance" , "Start Date", "End Date", "Total Price", "Status"))
        for rental in open_rentals:
            print(rental)
        if search_criteria == "1":
            return open_rentals[0]

    def fuel_status(self, car):
        tank_size = car.get_tank_size()
        while True:
            fuel_level = input("Fuel Status (G1 - G8): ").upper()
            if (fuel_level[0] == "G") and (fuel_level[1:] in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                break
            else:
                _ = input("Invalid input.\nPress Enter to continue...")
        num = int(fuel_level[-1])
        fuel_price = (((8 - num) / 8) * tank_size) * 250
        clear()
        return int(fuel_price), fuel_level

    def damage_check(self):
        while True:
            damage = input("Car damaged(Y/N): ").upper()
            if damage == "Y":
                print("Customer needs to fill out form AZ-190-TTS.")
                _ = input("Press Enter to continue...")
                return True
            elif damage == "N":
                _ = input("Car in perfect shape.\nPress Enter to continue...")
                return False
            else:
                _ = input("Invalid input.\Press Enter to continue...")

    def change_payment(self, payment):
        change = input("Change payment(Y/N): ").upper()
        if change == "Y":
            print("Payment methods:")
            print("\t1. Cash.")
            print("\t2. Credit Card")
            print("\t3. Debit Card.")
            choice = input("Preferred payment method: ")
            clear()
            if choice == "1":
                payment = "Cash"
            elif choice == "2":
                payment = "Credit Card"
            elif choice == "3":
                payment = "Debit Card"
        return payment

    def finish_order(self, rental, car, customer, fuel, damage):
        car_string = "{} {} ({})".format(car.get_make(), car.get_model(), car.get_license_plate())

        today = datetime.today()
        now = datetime(today.year, today.month, today.day)
        start_date= "{}/{}/{}".format(str(rental.get_start_date().day), str(rental.get_start_date().month), str(rental.get_start_date().year))
        end_date = "{}/{}/{}".format(str(now.day), str(now.month), str(now.year))
        delta = now - rental.get_start_date()
        days = int(delta.days)

        car_price = car.get_price() * days
        car_price_with_vat = int(car_price * 1.24)

        insurance_list = self.get_insurance_info(car.get_car_class(), rental.get_insurance())
        insurance_cost_per_day = insurance_list[0]
        insurance_cost = insurance_cost_per_day * days
        insurance_cost_w_vat = int(insurance_cost * 1.24)
        insurance_name = insurance_list[1]
        insurance_info = insurance_list[2]

        fuel_price = fuel[0]
        fuel_price_with_vat = int(fuel_price * 1.24)

        total_price = car_price + insurance_cost + fuel_price
        total_price_with_vat = car_price_with_vat + insurance_cost_w_vat + fuel_price_with_vat
        vat = total_price_with_vat - total_price

        payment = rental.get_payment()
        while True:
            print("{:<165}".format(rental.get_order_num()))
            print("{:<165}{:<20}".format(customer.get_name(), "HSST Rental Company"))
            print("{:<165}{:<20}".format(customer.get_soc_sec_num(), "SSN: 040499-2059"))
            print("{:<165}{:<20}".format(customer.get_home_address(), "Hvergiland 88"))
            print("{:<165}{:<20}".format(customer.get_email(), "hsst@hsst.is"))
            print("{:<165}{:<20}".format(customer.get_phone_num(), "Phone: 642-1000"))
            print("\n\n")
            print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Item", "Description", "Start Date", "Return Date", "Price per day",  "Total Price no VAT", "Total Price with VAT"))
            print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Car Rental", car_string, start_date, end_date, str(car.get_price()) + " kr", str(car_price) + " kr", str(car_price_with_vat) + " kr"))
            print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Insurance", insurance_name, "", "", str(insurance_cost_per_day) + " kr", str(insurance_cost) + " kr", str(insurance_cost_w_vat) + " kr"))
            for info in insurance_info:
                    print("{:<20}-{:<45}".format("", info))
            print("\n")

            print("{:<20}{:<55}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Fuel Cost", "Fuel Level: " + fuel[1], "", "", "", str(fuel_price) + " kr", str(fuel_price_with_vat) + " kr"))
            if damage == True:
                print("{:<20}{:<55}".format("Damage", "AZ-190-TTS Report sent to insurance department"))
            print("\n\n")
            print("{:.<100}{:.>85}".format("Total Price no VAT ", str(total_price) + " kr"))
            print("{:.<100}{:.>85}".format("VAT ", str(vat) + " kr"))
            print("{:.<100}{:.>85}".format("Total Price with VAT ", str(total_price_with_vat) + " kr"))
            print("\n\n")
            print("Payment: {}\n\n".format(payment))
            print("1. Confirm order")
            print("2. Change payment method")
            print("3. Back to main menu")
            choice = input("Input choice here: ")
            if choice == "1":
                pass
                # confirm order
            elif choice == "2":
                payment = self.change_payment(payment)
                clear()
            elif choice == "3":
                pass
            else:
                _ = input("Invalid input.\nPress Enter to continue...")






    def get_open_rental_for_car(self, car):
        return self.__rental_repo.get_open_rental_for_car(car)