class Car:
    def __init__(self, car_id, make, model, manuf_year, car_class, 
        seats, doors, color, transmission, fuel_type, price, tank_size, availability = True):
        self.__car_id = car_id
        self.__make = make
        self.__model = model
        self.__manuf_year = manuf_year
        self.__car_class = int(car_class)
        self.__seats = seats
        self.__doors = doors
        self.__color = color
        self.__transmission = transmission
        self.__fuel_type = fuel_type
        self.__tank_size = tank_size
        self.__price = int(price)
        self.__availability = availability

    def get_car_id(self):
        return self.__car_id

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

    def get_transmission(self):
        return self.__transmission

    def get_fuel_type(self):
        return self.__fuel_type

    def get_tank_size(self):
        return self.__tank_size

    def get_price(self):
        return self.__price

    def get_availability(self):
        return self.__availability

    def set_color(self, color):
        self.__color = color
    
    def set_transmission(self, transmission):
        self.__transmission = transmission

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type
        
    def set_tank_size(self, tank_size):
        self.__tank_size = tank_size

    def set_price(self, price):
        self.__price = price

    def set_availability(self, availability):
        self.__availability = availability
    
    def __str__(self):
        return "{:<10}{:<15}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}".format(self.__car_id, 
            self.__make, self.__model, self.__manuf_year, self.__car_class, self.__seats, self.__doors, 
            self.__color, self.__transmission, self.__price)
