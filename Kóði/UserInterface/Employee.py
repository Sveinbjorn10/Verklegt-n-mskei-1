from datetime import datetime
import os
clear = lambda: os.system('cls')


class Employee:

    def __init__(self):
        pass
        # self.__car_service = CarService()
        # self.__customer_service = CustomerService()
        # self.__rental_service = RentalService()

    def pick_date(self):
        while True:
                    go = True
                    date = input("Choose a starting date(DD/MM/YYYY): ")
                    date_list = [int(word) for word in date.split("/")]
                    
                    try:
                        start_date = datetime(date_list[2], date_list[1], date_list[0])
                    except:
                        go = False
                        _ = input("Invalid time period.\nPress any key to continue...")
                        clear()

                    if go == True:
                        date = input("Choose a return date(DD/MM/YYYY): ")
                        date_list = [int(word) for word in date.split("/")]
                        try:
                            return_date = datetime(date_list[2], date_list[1], date_list[0])
                            clear()
                            break
                        except:
                            _ = input("Invalid time period.\nPress any key to continue...")
                            clear()
        return start_date, return_date  

    def main_screen(self):
        action = ""
        while (action != "8"):
            print("Welcome to HSST Rental Software")
            print("\t1. Rent a car")
            print("\t2. Return a car")
            print("\t3. Available cars")
            print("\t4. Price list")
            print("\t5. Customer database")
            print("\t6. Car database")
            print("\t7. Rental database")
            print("\t8. Exit")
            action = input("Input choice here: ")

            if action == "1":
                clear()
                start_date, return_date = pick_date()
                
                            

                    

def main():
    employee = Employee()
    employee.main_screen()

main()