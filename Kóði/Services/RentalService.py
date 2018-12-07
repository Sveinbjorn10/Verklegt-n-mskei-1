from Repos.RentalRepo import RentalRepo
from datetime import datetime
import os

clear = lambda: os.system('cls')

class RentalService:
    def __init__(self):
        self.__rental_repo = RentalRepo()
    
    def pick_date(self):
        while True:
                    go = True
                    date = input("Choose a starting date(DD/MM/YYYY): ")
                    try:
                        date_list = [int(word) for word in date.split("/")]
                        start_date = datetime(date_list[2], date_list[1], date_list[0])
                    except:
                        go = False
                        _ = input("Invalid input.\nPress Enter to continue...")
                        clear()

                    if go == True:
                        date = input("Choose a return date(DD/MM/YYYY): ")
                        try:
                            date_list = [int(word) for word in date.split("/")]
                            return_date = datetime(date_list[2], date_list[1], date_list[0])
                            if return_date > start_date:
                                clear()
                                break
                            else:
                                _ = input("Invalid time period.\nPress Enter to continue...")
                                clear()
                        except:
                            _ = input("Invalid time period.\nPress Enter to continue...")
                            clear()
        return start_date, return_date  
    
    def pick_search_criteria(self, start, end):
        start_date = "{}/{}/{}".format(start.day, start.month, start.year)
        end_date = "{}/{}/{}".format(end.day, end.month, end.year)
        time_period = "({}) ---> ({})".format(start_date, end_date)
        while True:
            print(time_period)
            print("\t1. Car ID.")
            print("\t2. Search for car.")
            print("\t3. Return to menu.")
            choice = input("Input choice here: ")
            if choice in ["1", "2", "3"]:
                clear()
                return choice
            else:
                _ = input("Invalid input.\nPress Enter to continue...")
                clear()
        
    def search_car(self, start, end):
        start_date = "{}/{}/{}".format(start.day, start.month, start.year)
        end_date = "{}/{}/{}".format(end.day, end.month, end.year)
        time_period = "({}) ---> ({})".format(start_date, end_date)
        while True:
            print(time_period)
            print("Search for car:")
            print("\t1. Small car.")
            print("\t2. Family car.")
            print("\t3. Van.")
            print("\t4. SUV.")
            print("\t5. Every type.")
            print("\t6. Go back.")
            choice = input("Input choice here: ")
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return choice
            else: 
                _ = input("Invalid input.\nPress Enter to continue...")
                clear()