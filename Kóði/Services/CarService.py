from Repos.CarRepo import CarRepo
from Models.Car import Car
import os

clear = lambda: os.system('cls')

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()

    def print_car_database(self):
        print(self.__car_repo)

    def search_by_license_plate(self):
        return self.__car_repo.search_by_license_plate()

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

    def car_by_class(self, start, end):
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
                choice = int(choice)
                break
            else: 
                _ = input("Invalid input.\nPress Enter to continue...")
                clear()

        if choice == 6:
            return None
        available_cars = self.__car_repo.get_available_cars()

        if choice == 5:
            clear()
            return available_cars

        available_cars_in_class = []
        for car in available_cars:
            if car.get_car_class() == choice:
                available_cars_in_class.append(car)

        return available_cars_in_class
    
    def select_car(self, available_cars):
        # car_list = self.__car_repo.get_car_list()
        # # available_cars = [car for car in car_list if ((car[4] == car_class) and (car[-1] == "True"))]
        # available_cars = [car for car in car_list if (car.get_availability() == "True") and (car.get_car_class() == car_class)]
        # clear()
        while True:
            clear()
            print("Available cars")
            print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ","Nr.", "License", "Make", "Model", "Manuf. Year", "Seats", "Doors", "Color", "Transmission", "Fuel", "Price per day"))
            for index, car in enumerate(available_cars):
                print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ", (index + 1), car.get_license_plate(), car.get_make(), car.get_model(), car.get_manuf_year(), car.get_seats(), car.get_doors(), car.get_color(), car.get_transmission(), car.get_fuel_type(), car.get_price()))
            try:
                car_choice = int(input("Select a car: "))
                if (car_choice > 0) and (car_choice <= len(available_cars)):
                    
                    return available_cars[car_choice - 1]
                else:
                    _ = input("Invalid input!\nPress Enter to continue...")
                    # clear()
            except:
                _ = input("Invalid input!\nPress Enter to continue...")
                clear()

    def get_available_cars_database(self, available_cars):
        print("Available cars")
        print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ", 
            "Nr.", "License", "Make", "Model", "Manuf. Year", "Seats", "Doors", "Color", 
            "Transmission", "Fuel", "Price per day"))
        for index, car in enumerate(available_cars):
            print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ", 
                (index + 1), car.get_license_plate(), car.get_make(), car.get_model(), 
                car.get_manuf_year(), car.get_seats(), car.get_doors(), car.get_color(), 
                car.get_transmission(), car.get_fuel_type(), car.get_price()))
        print()

    def get_available_cars(self):
        return self.__car_repo.get_available_cars()

    def print_car_database_menu(self):
        print("\t1. View Car Database")
        print("\t2. Add Car")
        print("\t3. Edit Car")
        print("\t4. Delete Car")
        print("\t5. Return to Main Menu")

    def car_info(self):
        print("New Car")
        license_plate = input("\tLicense Plate: ")
        make = input("\tMake: ")
        model = input("\tModel: ")
        manuf_year = input("\tManufacturing Year: ")
        car_class = int(input("\tCar Class: "))
        seats = int(input("\tSeats: "))
        doors = int(input("\tDoors: "))
        color = input("\tColor: ")
        weight = input("\tWeight: ")
        engine_size = input("\tEngine Size: ")
        horse_power = input("\tHorse Power: ")
        transmission = input("\tTransmission: ")
        fuel_type = input("\tFuel Type: ")
        price = int(input("\tPrice: "))
        drive = input("\tDrive: ")
        total_km = int(input("\tTotal Kilometers: "))
        tank_size = input("\tTank Size: ")
        availability = True
        new_car = Car(license_plate, make, model, manuf_year, car_class, 
            seats, doors, color, weight, engine_size,  
            horse_power, transmission, fuel_type, price, 
            drive, total_km, tank_size, availability)
        self.__car_repo.add_car(new_car)

    def update_car_info(self, car_id):
        return self.__car_repo.update_car_info(car_id)

    def delete_car(self, car_id):
        return self.__car_repo.delete_car(car_id)

    def print_price_options(self):
        print("\t1. Print car prices")
        print("\t2. Print Insurance prices")
        print("\t3. Return to main menu")


    def print_car_price_list(self):
        print("{:<33s}{:<33s}{:<21}".format("Car class", "Price per day", "Car make e.g"))
        print("-" * 100)
        print("{:<33s}{:<33s}{:<21}".format("Small Car", "10.000kr", "VW Golf"))
        print("{:<33s}{:<33s}{:<21}\n".format("", "", "Hyundai i10"))
        print("{:<33s}{:<33s}{:<21}".format("Family Car", "14.000kr", "Toyota Corolla"))
        print("{:<33s}{:<33s}{:<21}\n".format("", "", "Skoda Octavia"))
        print("{:<33s}{:<33s}{:<21}".format("Van", "25.000kr", "Ford Galaxy"))
        print("{:<33s}{:<33s}{:<21}".format("", "", "Renault Traffic3"))
        print("{:<33s}{:<33s}{:<21}\n".format("", "", "VW Caravelle 4wd"))
        print("{:<33s}{:<33s}{:<21}".format("Suv", "20.000kr", "Audi Q5"))
        print("{:<33s}{:<33s}{:<21}".format("", "", "Toyota Landcruiser"))
        print("{:<33s}{:<33s}{:<21}\n".format("", "", "Toyota Rav4"))

    def print_insurance_price_list(self):
        print("{:<45}{:^25}{:^25}{:^25}".format("Insurance Name:", "Included Insurance", "Insurance Package 1", "Insurance Package 2"))
        print("-" * 140)
        print("{:<45}{:^25}{:^25}{:^25}".format("Collision Damage Waiver (CDW)", "YES", "YES", "YES"))
        print("{:<45}{:^25}{:^25}{:^25}".format("Driver + Passenger Injury Insurance (PAI)", "YES", "YES", "YES"))
        print("{:<45}{:^25}{:^25}{:^25}".format("Third Party Insurance (TP)", "YES", "YES", "YES"))
        print("{:<45}{:^26}{:^24}{:^25}".format("Super Collision Damage Waiver (SCDW)", "NO", "YES", "YES"))
        print("{:<45}{:^26}{:^24}{:^25}".format("Windshield Insurance (GP)", "NO", "YES", "YES"))
        print("{:<45}{:^26}{:^25}{:^24}".format("Sand And Dust Waiver (SADW)", "NO", "NO", "YES"))
        print("{:<45}{:^26}{:^25}{:^24}".format("No Deductable Insurance (ZERO)", "NO", "NO", "YES"))
        print()
        print()
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance price per day:", "Small Car", "Family Car", "Van", "SUV"))
        print("-" * 140)
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance Package 1", "2.000kr", "2.000kr", "3.750kr", "3.300kr"))
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance package 2", "3.750kr", "3.750kr", "6.000kr", "5.500kr"))
        print()
        print()
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Max Deductable Insurance:", "Small Car", "Family Car", "Van", "SUV"))
        print("-" * 140)
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Included Insurance", "195.000kr", "195.000kr", "395.000kr", "375.000kr"))
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance Package 1", "49.500kr", "49.500kr", "105.000kr", "95.000kr"))
        print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance package 2", "0kr", "0kr", "0kr", "0kr"))
        _ = input()