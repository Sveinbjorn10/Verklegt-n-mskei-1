from Models.Car import Car

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
            with open("./Data/cars.csv", "r") as car_file:
                for line in car_file.readlines():
                    (license_plate, make, model, manuf_year, car_class, seats, doors, color, weight, 
                        engine_size, horse_power, transmission, fuel_type, price, drive, total_km, 
                        tank_size, availability) = line.split(",")
                    new_car = Car(license_plate, make, model, manuf_year, car_class, seats, doors, 
                        color, weight, engine_size, horse_power, transmission, fuel_type, price, drive, 
                        total_km, tank_size, availability)
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
            if car[2] == car_class:
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
            if car[0] == license_plate:
                all_cars.pop(index)
        with open("./Data/cars.csv", "w") as f:
            for car in all_cars:
                f.write(car)

    def get_available_cars(self, availability):
        return_list = []
        all_cars = self.get_cars()
        for car in all_cars:
            if car[-1] == True:
                return_list.append(car)
        return return_list


# + update_car_info()
# + change_car_status()