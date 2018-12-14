class Car:
    def __init__(self, license_plate, make, model, manuf_year, car_class, 
        seats, doors, color, weight, engine_size, horse_power, transmission, 
        fuel_type, price, drive, total_km, tank_size, availability = True):
        self.__license_plate = license_plate
        self.__make = make
        self.__model = model
        self.__manuf_year = manuf_year
        self.__car_class = int(car_class)
        self.__seats = seats
        self.__doors = doors
        self.__color = color
        self.__weight = weight
        self.__engine_size = engine_size
        self.__horse_power = horse_power
        self.__transmission = transmission
        self.__fuel_type = fuel_type
        self.__drive = drive
        self.__total_km = total_km
        self.__tank_size = int(tank_size)
        self.__price = int(price)
        self.__availability = availability

    def get_license_plate(self):
        return self.__license_plate

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model

    def get_manuf_year(self):
        return self.__manuf_year

    def get_car_class(self):
        return self.__car_class

    def get_seats(self):
        return self.__seats

    def get_doors(self):
        return self.__doors

    def get_color(self):
        return self.__color

    def get_weight(self):
        return self.__weight

    def get_engine_size(self):
        return self.__engine_size

    def get_horse_power(self):
        return self.__horse_power
    
    def get_transmission(self):
        return self.__transmission

    def get_fuel_type(self):
        return self.__fuel_type
        
    def get_drive(self):
        return self.__drive

    def get_total_km(self):
        return self.__total_km

    def get_tank_size(self):
        return self.__tank_size

    def get_price(self):
        return self.__price

    def get_availability(self):
        return self.__availability

    def set_color(self, color):
        self.__color = color

    def set_weight(self, weight):
        self.__weight = weight

    def set_engine_size(self, engine_size):
        self.__engine_size = engine_size

    def set_horse_power(self, horse_power):
        self.__horse_power = horse_power
    
    def set_transmission(self, transmission):
        self.__transmission = transmission

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type
        
    def set_drive(self, drive):
        self.__drive = drive

    def set_total_km(self, total_km):
        self.__total_km = total_km

    def set_tank_size(self, tank_size):
        self.__tank_size = tank_size

    def set_price(self, price):
        self.__price = price

    def set_availability(self, availability):
        self.__availability = availability
    
    def __str__(self):
        return "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}".format(self.__license_plate, 
            self.__make, self.__model, self.__manuf_year, self.__car_class, self.__seats, self.__doors, 
            self.__color, self.__transmission, self.__price)
