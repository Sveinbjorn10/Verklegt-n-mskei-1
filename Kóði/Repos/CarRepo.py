from Models.Car import Car
import csv

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
                    availability = "True"
                    new_car = Car(license_plate, make, model, manuf_year, car_class, seats, doors, 
                        color, weight, engine_size, horse_power, transmission, fuel_type, price, drive, 
                        total_km, tank_size, eval(availability))
                    self.__cars.append(new_car)    
        return self.__cars

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