class Car:
    def __init__(self, license_plate, make, model, manuf_year, car_class, 
        seats, doors, color, weight, engine_size, horse_power, transmission, 
        fuel_type, price, drive, total_km, tank_size, availability = True):
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.manuf_year = manuf_year
        self.car_class = car_class
        self.seats = seats
        self.doors = doors
        self.color = color
        self.weight = weight
        self.engine_size = engine_size
        self.horse_power = horse_power
        self.transmission = transmission
        self.fuel_type = fuel_type
        self.drive = drive
        self.total_km = total_km
        self.tank_size = tank_size
        self.price = price
        self.availability = availability
