import csv
from datetime import datetime
import os

os.system('mode con: cols=190 lines=40')

#     def print_order_confirmation(self, customer, car, insurance, payment, start, end, additional_driver = "Empty"):
#         delta = end - start
#         days = int(delta.days)

#         order_number = self.get_order_number()
#         name = customer.get_name()
#         ssn = customer.get_soc_sec_num()
#         home_address = customer.get_home_address()
#         email = customer.get_email()
#         phone = customer.get_phone_num()

#         if additional_driver != "Empty":    
#             additional_driver_name = "{} {}".format(additional_driver[0], additional_driver[1])
#             additional_driver_ssn = additional_driver[2]
#             additional_driver_driv_license = additional_driver[3]

#         car_make = car.get_make()
#         car_model = car.get_model()
#         car_plate = car.get_license_plate()
#         car_price_per_day = car.get_price()

#         car_price = car_price_per_day * days
#         car_price_w_vat = float(car_price * 1.24)
#         car_string = "{} {} ({})".format(car_make, car_model, car_plate)
#         car_class = car.get_car_class()

#         insurance_list = self.get_insurance_info(car_class, insurance)
#         insurance_cost_per_day = int(insurance_list[0])
#         insurance_cost = insurance_cost_per_day * days
#         insurance_cost_w_vat = float(insurance_cost * 1.24)
#         insurance_name = insurance_list[1]
#         insurance_info = insurance_list[2]

#         total_price = car_price + insurance_cost
#         vat = float(total_price * 0.24)
#         total_price_w_vat = float(total_price * 1.24)

print("{:<10}".format("ON18-00001"))
print("{:<165}{:<20}".format("Sveinbjörn Jóhanneson", "HSST Rental Company"))
print("{:<165}{:<20}".format("1404983359", "SSN: 040499-2059"))
print("{:<165}{:<20}".format("Dimmuhvarf 5", "Hvergiland 88"))
print("{:<165}{:<20}".format("sveinbjornj18@ru.is", "hsst@hsst.is"))
print("{:<165}{:<20}".format("8521927", "Phone: 642-1000"))
print("\n\n")
print("{:<30}{:<45}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Item", "Description", "Start Date", "Return Date", "Price per day",  "Total Price no VAT", "Total Price with VAT"))
print("{:<30}{:<45}{:<20}{:<20}{:<20}{:<30}{:<20}".format("Car Rental", "Volkswagen Transporter (AF 315)", "12/12/2018", "13/12/2018", "10.000" + " kr", "10.000" + " kr", "12.400" + " kr"))
_ = input()
print("{:<30}{:<45}{:<20}{:<20}{:<20} kr{:<30} kr{:<20} kr".format("Insurance", insurance_name, "", "", insurance_cost_per_day, insurance_cost, insurance_cost_w_vat))

for info in insurance_info:
        print("{:<15}-{:<45}".format("", info))


#Additional driver here
if additional_driver != "Empty": 
        print("{:<30}{:<45}".format("Additional Driver", additional_driver_name))
        print("{:<30}SSN: {:<45}".format("", additional_driver_ssn))
        print("{:<30}Drivers License: {:<45}".format("", additional_driver_driv_license))

print("\n\n")
print("{:.<100}{:.>70} kr".format("Total Price no VAT ", total_price))
print("{:.<100}{:.>70} kr".format("VAT ", vat))
print("{:.<100}{:.>70} kr".format("Total Price with VAT ", total_price_w_vat))
print("\n\n")
print("Payment: {}".format(payment))
_ = input()