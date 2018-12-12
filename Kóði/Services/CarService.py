from Repos.CarRepo import CarRepo

class CarService:
    def __init__(self):
        self.__car_repo = CarRepo()

    def print_car_database(self):
        print(self.__car_repo)

    # def price_list(self):
