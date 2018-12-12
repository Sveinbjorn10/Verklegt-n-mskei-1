from Repos.CarRepo import CarRepo
from Models.Car import Car
import os

clear = lambda: os.system('cls')

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()

    def print_car_database(self):
        print(self.__car_repo)

    def search_by_license_plate(self, license_plate):
        return self.__car_repo.search_by_license_plate(license_plate)

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
                    clear()
            except:
                _ = input("Invalid input!\nPress Enter to continue...")
                clear()