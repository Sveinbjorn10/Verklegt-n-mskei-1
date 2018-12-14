from Models.Car import Car
import os
import csv
clear = lambda: os.system('cls')

class CarRepo:

    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        # first add to file then to private list
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
                    availability = "True" #Möguleiki á villum
                    new_car = Car(car_id, make, model, manuf_year, car_class, seats, doors, 
                        color, transmission, fuel_type, price, tank_size, eval(availability))
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
        car_class = input("Enter Car Class: ")
        all_cars = self.get_cars()
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
            if car.get_car_id == car_id:
                all_cars.pop(index)
        with open("./Data/cars.csv", "w") as car_file:
            car_file.truncate()
            car_writer = csv.writer(car_file)
            for row in all_cars:
                car_writer.writerow(row)

    def get_available_cars(self):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_availability() == True:
                return_list.append(car)
        return return_list

    def search_by_car_id(self):
        car_id = input("Enter Car ID: ")
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

    def change_car_status(self, car_id):
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_car_id == car_id:
                car_availability = car.get_availability()
                if car_availability == True:
                    return car.set_availability(False)
                else:
                    return car.set_availability(True)

    def update_car_info(self, driver_license):
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_car_id == driver_license:
                edit_car = car
                print(edit_car)
                print("1. Edit Color\n2. Edit Transmission\n"
                        "3. Edit Fuel Type\n4. Edit Tank Size\n5. Edit Price\n6. Return to Main Menu")
                while True:   
                    choice = input("What do you want to change:")
                    if (choice < 1) or (choice > 6):
                        print("Invalid Input")
                        _ = input("Press Enter to continue...")
                        clear()
                    else:
                        break
                while True:
                    if choice == 1:
                        print("Current Color: {}".format(edit_car.get_color()))
                        new_color = input("New color: ")
                        edit_car.set_color(new_color)
                        print("New Current Color: {}".format(edit_car.get_color()))
                    if choice == 2:
                        print("Current Transmission: {}".format(edit_car.get_transmission()))
                        new_transmission = input("New Transmission: ")
                        edit_car.set_transmission(new_transmission)
                        print("New Current Transmission: {}".format(edit_car.get_transmission()))
                    if choice == 3:
                        print("Current Fuel Type: {}".format(edit_car.get_fuel_type()))
                        new_fuel_type = input("New Fuel Type: ")
                        edit_car.set_fuel_type(new_fuel_type)
                        print("New Current Fuel Type: {}".format(edit_car.get_fuel_type()))
                    if choice == 4:
                        print("Current Tank Size: {}".format(edit_car.get_tank_size()))
                        new_tank_size = input("New Tank Size: ")
                        edit_car.set_tank_size(new_tank_size)
                        print("New Current Tank Size: {}".format(edit_car.get_tank_size()))
                    if choice == 5:
                        print("Current Price: {}".format(edit_car.get_price()))
                        new_price = input("New Price: ")
                        edit_car.set_price(new_price)
                        print("New Current Price: {}".format(edit_car.get_drive()))
                    if choice == 6:
                        break

    def __str__(self):
<<<<<<< HEAD
        string = "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}\n".format("License:", "Make:", 
            "Model:", "Manuf. Year:", "Car Class:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:")
=======
        string = "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}\n{}\n".format("License:", "Make:", 
            "Model:", "Car Class:", "Manuf. Year:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:", "-"*121)
>>>>>>> 0662460e8a89b32edd3690d19aa4d0241e3c2655
        carlist = self.get_cars()
        for car in carlist:
            string += str(car) + "\n"
        return string

    def get_car_list(self):
        car_list = []
        car_class_list = []
        with open("./data/cars.csv") as cars:
            csv_reader = csv.reader(cars)
            for car in csv_reader:
                car_list.append(car)
            for line in car_list:
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
                availability = "True"
                new_car = Car(car_id, make, model, manuf_year, car_class, seats, doors, 
                        color, transmission, fuel_type, price, tank_size, eval(availability))
                car_class_list.append(new_car)
        return car_class_list
