import sys
import os

clear = lambda: os.system('cls')
os.system('mode con: cols=135 lines=40')

def print_list(my_list):
    print("Available cars")
    print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ","Nr.", "License", "Make", "Model", "Manuf. Year", "Seats", "Doors", "Color", "Transmission", "Fuel", "Price per day"))
    for index, car in enumerate(my_list):
        print("{:5}{:<5}{:<10}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format(" ", (index + 1), car[0], car[1], car[2], car[3], car[5], car[6], car[7], car[11], car[12], car[13]))
    # selection = input("Select a car: ")
# args = sys.argv[1:]

# car_class = args[0]
car_class = "3"

with open("Data/cars.csv", "r", encoding = "utf-8") as f:
    temp_list = [line.strip() for line in f.readlines()]
    while True:
        car_list = []
        available_cars = []
        # temp_list = [line.strip() for line in f.readlines()]
        for car in temp_list:
            temp = car.split(",")
            car_list.append(temp)
        for car in car_list:
            if (car[4] == car_class) and (car[-1] == "True"):
                available_cars.append(car)
        print_list(available_cars)
        try:
            car_selection = int(input("Select a car: "))
            if car_selection in range(len(available_cars)+1):
                print(available_cars[car_selection-1])
                _ = input("Press Enter to continue...")
                with open("selected_car.txt", "w", encoding = "utf-8") as f:
                    f.write(available_cars[car_selection-1][0])
                break
            else:
                _ = input("Invalid input!\nPress Enter to continue...")
                clear()
        except:
            _ = input("Invalid input!\nPress Enter to continue...")
            clear()
        
# Möguleiki að henda upplýsingum í temp skjal og taka svo upplýsingarnar þaðana seinna....