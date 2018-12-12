class Rental:
    def __init__(self, order_num, name, soc_sec_num, license_plate, insurance, 
        start_date, end_date, total_price):
        self.__order_num = order_num
        self.__name = name
        self.__soc_sec_num = soc_sec_num
        self.__license_plate = license_plate
        self.__insurance = insurance
        self.__start_date = start_date
        self.__end_date = end_date
        self.__total_price = total_price

    def get_order_num(self):
        return self.__order_num

    def get_name(self):
        return self.__name
    
    def get_soc_sec_num(self):
        return self.__soc_sec_num

    def get_license_plate(self):
        return self.__license_plate

    def get_insurance(self):
        return self.__insurance

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_total_price(self):
        return self.__total_price



    def __str__(self):
        return "{:<15}{:<30}{:<12}{:<15}{:<20}{:<12}{:<12}{:<20}".format(self.__order_num, 
            self.__name, self.__soc_sec_num, self.__license_plate, self.__insurance, 
            self.__start_date, self.__end_date, self.__total_price)