from datetime import datetime
class Rental:
    def __init__(self, order_num, name, soc_sec_num, car_id, insurance, 
        start_date, end_date, total_price, status, payment):
        self.__order_num = order_num
        self.__name = name
        self.__soc_sec_num = soc_sec_num
        self.__car_id = car_id
        self.__insurance = insurance
        self.__start_date = datetime(int(start_date[6:]), int(start_date[3:5]), int(start_date[0:2])) 
        self.__end_date = end_date
        self.__total_price = total_price
        self.__status = status
        self.__payment = payment

    def get_order_num(self):
        return self.__order_num

    def get_name(self):
        return self.__name
    
    def get_soc_sec_num(self):
        return self.__soc_sec_num

    def get_car_id(self):
        return self.__car_id

    def get_insurance(self):
        return self.__insurance

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_total_price(self):
        return self.__total_price

    def get_status(self):
        return self.__status
    
    def get_payment(self):
        return self.__payment



    def __str__(self):
        return "{:<15}{:<30}{:<12}{:<15}{:<20}{:<12}{:<12}{:<20}{:<5}".format(self.__order_num, 
            self.__name, self.__soc_sec_num, self.__car_id, self.__insurance, 
            self.__start_date, self.__end_date, self.__total_price + " kr", self.__status)