from Models.Rental import Rental
import csv
class RentalRepo:

    def __init__(self):
        self.__rentals = []

    def add_rental(self, rental):
        with open("./Data/rentals.csv", "a+", encoding = "utf-8") as rental_file:
            order_num = rental.get_order_num()
            name = rental.get_name()
            ssn = rental.get_soc_sec_num()
            license_plate = rental.get_license_plate()
            insurance = rental.get_insurance()
            start_date = rental.get_start_date()
            end_date = rental.get_end_date()
            total_price = rental.get_total_price()
            rental_file.write("{},{},{},{},{},{},{},{}\n".format(order_num, name, ssn, license_plate, insurance, start_date, end_date, total_price))

    def get_rental_list(self):
        if self.__rentals == []:
            with open("./data/rentals.csv", "r", encoding = "utf-8") as rental_file:
                rental_reader = csv.reader(rental_file)
                for line in rental_reader:
                    order_num = line[0]
                    name = line[1]
                    soc_sec_num = line[2]
                    license_plate = line[3]
                    insurance = line[4]
                    start_date = line[5]
                    end_date = line[6]
                    total_price = line[7]
                    new_rental = Rental(order_num, name, soc_sec_num, license_plate, insurance, start_date, end_date, 
                        total_price)
                    self.__rentals.append(new_rental)    
        return self.__rentals
    
    def search_by_cust_name(self, name):
        return_list = []
        all_rentals = self.get_rental_list()
        for rental in all_rentals:
            if rental[1] == name:
                return_list.append(rental)
        return return_list
    
    def search_by_cust_ssn(self, soc_sec_num):
        return_list = []
        all_rentals = self.get_rental_list()
        for rental in all_rentals:
            if rental[2] == soc_sec_num:
                return_list.append(rental)
        return return_list

    def search_by_license_plate(self, license_plate):
        return_list = []
        all_rentals = self.get_rental_list()
        for rental in all_rentals:
            if rental[3] == license_plate:
                return_list.append(rental)
        return return_list

    def __str__(self):
        string = "{:<15}{:<30}{:<12}{:<15}{:<20}{:<12}{:<12}{:<20}\n".format("Order Number:", "Name:", 
            "SSN:", "License Plate:", "Insurance:" , "Start Date:", "End Date:", "Total Price:")
        rentallist = self.get_rental_list()
        for rental in rentallist:
            string += str(rental) + "\n"
        return string

