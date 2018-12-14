from Models.Car import Car
import os
import csv
clear = lambda: os.system('cls')

class CarRepo:

    def __init__(self):
        self.__cars = []

    def add_car(self, car, not_in_delete = True):
        # first add to file then to private list
        if not_in_delete == True:
            self.__cars.append(car)
        with open("./data/cars.csv", "a+") as car_file:
            car_id = car.get_car_id()
            make = car.get_make()
            model = car.get_model()
            manuf_year = car.get_manuf_year()
            car_class = car.get_car_class()
            seats = car.get_seats()
            doors = car.get_doors()
            color = car.get_color()
            transmission = car.get_transmission()
            fuel_type = car.get_fuel_type()
            price = car.get_price()
            tank_size = car.get_tank_size()
            availability = car.get_availability()
            car_file.write("{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(car_id, 
                make, model, manuf_year, car_class, seats, doors, color, 
                transmission, fuel_type, price, tank_size, availability))

    def get_cars(self):
        if self.__cars == []:
            with open("./Data/cars.csv", "r", encoding = "utf-8") as car_file:
                car_reader = csv.reader(car_file)
                for line in car_reader:
                    car_id = line[0]
                    make = line[1]
                    model = line[2]
                    manuf_year = line[3]
                    car_class = line[4]
                    seats = line[5]
                    doors = line[6]
                    color = line[7]
                    transmission = line[8]
                    fuel_type = line[9]
                    price = line[10]
                    tank_size = line[11]
                    availability = line[12]
                    new_car = Car(car_id, make, model, manuf_year, car_class, seats, doors, 
                        color, transmission, fuel_type, price, tank_size, availability)
                    self.__cars.append(new_car)    
        return self.__cars

    def all_cars(self):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            return_list.append(car)
        return return_list

    def search_by_class(self):
        return_list = []
        all_cars = self.get_cars()
        while True:
            car_class = input("Enter Car Class: ")
            if car_class in ["1", "2", "3", "4"]:
                break
            else:
                _ = input("Invalid input.\nPress Enter to continue...")
                clear()
        for car in all_cars:
            if car.get_car_class() == int(car_class):
                return_list.append(car)
        return return_list

    def search_by_model(self):
        return_list = []
        model = input("Enter Car Model: ")
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_model() == model:
                return_list.append(car)
        return return_list

    def delete_car(self, car_id):
        all_cars = self.get_cars()
        for index, car in enumerate(all_cars):
            if car.get_car_id() == car_id:
                all_cars.pop(index)
        with open("./Data/cars.csv", "w", encoding = "utf-8") as car_file:
            car_file.truncate()
            for car in all_cars:
                self.add_car(car, False)
        clear()

    def get_available_cars(self):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_availability() == "Yes":
                return_list.append(car)
        return return_list

    def search_by_car_id(self):
        car_id = input("Enter Car ID: ").upper()
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_car_id() == car_id:
                string = "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}\n".format("License:", "Make:", 
                    "Model:", "Manuf. Year:", "Car Class:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:")
                print("{}{}".format(string, car))
                _ = input("Press Enter to continue...")
                return car
        input("Car not found!\nPress Enter to continue...")
        return None

    def change_car_status(self, car_id): #Breyta þessu all svakalega
        update_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_car_id() == car_id:
                car_availability = car.get_availability()
                if car_availability == "Yes":
                    car.set_availability("No")
                    update_list.append(car)
                else:
                    car.set_availability("Yes")
                    update_list.append(car)
            else:
                update_list.append(car)
        with open("./Data/cars.csv", "w", encoding = "utf-8") as car_file:
            car_file.truncate()
            for car in update_list:
                self.add_car(car)

    def update_car_info(self, car_id):
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_car_id() == car_id:
                string = "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}\n".format("License:", "Make:", 
                    "Model:", "Manuf. Year:", "Car Class:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:")
                edit_car = car
                print("{}{}\n".format(string, edit_car))
                print("1. Edit Color\n2. Edit Transmission\n3. Edit Price\n"
                    "4. Return to Main Menu")
                while True:
                    choice = input("What do you want to change: ")
                    if (int(choice) < 1) or (int(choice) > 6):
                        print("Invalid Input")
                        _ = input("Press Enter to continue...")
                        clear()
                    else:
                        break
                while True:
                    if choice == "1":
                        print("Current Color: {}".format(edit_car.get_color()))
                        new_color = input("New color: ")
                        edit_car.set_color(new_color)
                        print("Color Changed To: {}".format(edit_car.get_color()))
                        _ = input("Press Enter To Return To Main Menu...")
                        break
                    if choice == "2":
                        print("Current Transmission: {}".format(edit_car.get_transmission()))
                        new_transmission = input("New Transmission: ")
                        edit_car.set_transmission(new_transmission)
                        print("Transmission Changed To: {}".format(edit_car.get_transmission()))
                        _ = input("Press Enter To Return To Main Menu...")
                        break
                    if choice == "3":
                        print("Current Price: {}".format(edit_car.get_price()))
                        new_price = input("New Price: ")
                        edit_car.set_price(new_price)
                        print("Price Changed To: {}".format(edit_car.get_price()))
                        _ = input("Press Enter To Return To Main Menu...")
                        break
                    if choice == "4":
                        break

    def __str__(self):
        string = "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}\n".format("License:", "Make:", 
            "Model:", "Manuf. Year:", "Car Class:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:")
        carlist = self.get_cars()
        for car in carlist:
            string += str(car) + "\n"
        return string

    def get_car_for_rental(self, rental):
        car_list = self.get_cars()
        for car in car_list:
            if car.get_car_id() == rental.get_car_id():
                return car