from UserInterface.Employee import Employee
import os
os.system('mode con: cols=200 lines=40')
def main():
    ui = Employee()
    ui.main_screen()

main()