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
            license_plate = car.get_license_plate()
            make = car.get_make()
            model = car.get_model()
            manuf_year = car.get_manuf_year()
            car_class = car.get_car_class()
            seats = car.get_seats()
            doors = car.get_doors()
            color = car.get_color()
            weight = car.get_weight()
            engine_size = car.get_engine_size()
            horse_power = car.get_horse_power()
            transmission = car.get_transmission()
            fuel_type = car.get_fuel_type()
            price = car.get_price()
            drive = car.get_drive()
            total_km = car.get_total_km()
            tank_size = car.get_tank_size()
            availability = car.get_availability()
            car_file.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(license_plate, 
                make, model, manuf_year, car_class, seats, doors, color, weight, 
                engine_size, horse_power, transmission, fuel_type, price, drive, total_km, 
                tank_size, availability))

    def get_cars(self):
        if self.__cars == []:
            with open("./Data/cars.csv", "r", encoding = "utf-8") as car_file:
                car_reader = csv.reader(car_file)
                for line in car_reader:
                    license_plate = line[0]
                    make = line[1]
                    model = line[2]
                    manuf_year = line[3]
                    car_class = line[4]
                    seats = line[5]
                    doors = line[6]
                    color = line[7]
                    weight = line[8]
                    engine_size = line[9]
                    horse_power = line[10]
                    transmission = line[11]
                    fuel_type = line[12]
                    price = line[13]
                    drive = line[14]
                    total_km = line[15]
                    tank_size = line[16]
                    availability = "True" #Möguleiki á villum
                    new_car = Car(license_plate, make, model, manuf_year, car_class, seats, doors, 
                        color, weight, engine_size, horse_power, transmission, fuel_type, price, drive, 
                        total_km, tank_size, eval(availability))
                    self.__cars.append(new_car)    
        return self.__cars

    def all_cars(self):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            return_list.append(car)
        return return_list

    def search_by_class(self, car_class):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_car_class() == car_class:
                return_list.append(car)
        return return_list

    def search_by_model(self, model):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            if car[3] == model:
                return_list.append(car)
        return return_list

    def delete_car(self, license_plate):
        all_cars = self.get_cars()
        for index, car in enumerate(all_cars):
            if car.get_license_plate == license_plate:
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

    def search_by_license_plate(self):
        license_plate = input("Enter Car ID: ")
        all_cars = self.get_cars()
        for car in all_cars:
            if car.get_license_plate() == license_plate:
                return car
            else:
                input("Car not found!\nPress Enter to continue...")
                return None

    def change_car_status(self, license_plate):
        all_cars = self.get_cars()
        for car in all_cars:
            if car[0] == license_plate:
                car_availability = car.get_availability()
                if car_availability == True:
                    return car.set_availability(False)
                else:
                    return car.set_availability(True)

    def update_car_info(self, driver_license):
        all_cars = self.get_cars()
        for car in all_cars:
            if car[0] == driver_license:
                edit_car = car[0]
                print(edit_car)
                print("1. Edit Color\n2. Edit Weight\n3. Edit Engine Size\n"
                        "4. Edit Horse Power\n5. Edit Transmission\n"
                        "6. Edit Fuel Type\n7. Edit Drive\n8. Edit Total km\n"
                        "9. Edit Tank Size\n10. Edit Price\n11. Quit")
                while True:   
                    choice = input("What do you want to change:")
                    if (choice < 1) or (choice > 11):
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
                        print("Current Weight: {}".format(edit_car.get_weight()))
                        new_weight = input("New Weight: ")
                        edit_car.set_weight(new_weight)
                        print("New Current Weight: {}".format(edit_car.get_weight()))
                    if choice == 3:
                        print("Current Engine Size: {}".format(edit_car.get_engine_size()))
                        new_engine_size = input("New Engine Size: ")
                        edit_car.set_engine_size(new_engine_size)
                        print("New Current Engine Size: {}".format(edit_car.get_engine_size()))
                    if choice == 4:
                        print("Current Horse Power: {}".format(edit_car.get_horse_power()))
                        new_hp = input("New Horse Power: ")
                        edit_car.set_horse_power(new_hp)
                        print("New Current Horse Power: {}".format(edit_car.get_horse_power()))
                    if choice == 5:
                        print("Current Transmission: {}".format(edit_car.get_transmission()))
                        new_transmission = input("New Transmission: ")
                        edit_car.set_transmission(new_transmission)
                        print("New Current Transmission: {}".format(edit_car.get_transmission()))
                    if choice == 6:
                        print("Current Fuel Type: {}".format(edit_car.get_fuel_type()))
                        new_fuel_type = input("New Fuel Type: ")
                        edit_car.set_fuel_type(new_fuel_type)
                        print("New Current Fuel Type: {}".format(edit_car.get_fuel_type()))
                    if choice == 7:
                        print("Current Drive: {}".format(edit_car.get_drive()))
                        new_drive = input("New Drive: ")
                        edit_car.set_drive(new_drive)
                        print("New Current Drive: {}".format(edit_car.get_drive()))
                    if choice == 8:
                        print("Current Total km: {}".format(edit_car.get_total_km()))
                        new_total_km = input("New Total km: ")
                        edit_car.set_total_km(new_total_km)
                        print("New Current Total km: {}".format(edit_car.get_total_km()))
                    if choice == 9:
                        print("Current Tank Size: {}".format(edit_car.get_tank_size()))
                        new_tank_size = input("New Tank Size: ")
                        edit_car.set_tank_size(new_tank_size)
                        print("New Current Tank Size: {}".format(edit_car.get_tank_size()))
                    if choice == 10:
                        print("Current Price: {}".format(edit_car.get_price()))
                        new_price = input("New Price: ")
                        edit_car.set_price(new_price)
                        print("New Current Price: {}".format(edit_car.get_drive()))
                    if choice == 11:
                        break

    def __str__(self):
        string = "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}\n{}\n".format("License:", "Make:", 
            "Model:", "Car Class:", "Manuf. Year:", "Seats:", "Doors:", "Color:", "Transmission:", "Price:", "-"*121)
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
            for car in car_list:
                new_car = Car(car[0], car[1], car[2], car[3], car[4], car[5], car[6], car[7], car[8], car[9], car[10], car[11], car[12], car[13], car[14], car[15], car[16], car[17])
                car_class_list.append(new_car)
        return car_class_list
