import os

os.system('mode con: cols=140 lines=30')

print("{:<45}{:^25}{:^25}{:^25}".format("Insurance Name:", "Included Insurance", "Insurance Package 1", "Insurance Package 2"))
print("-" * 140)
print("{:<45}{:^25}{:^25}{:^25}".format("Collision Damage Waiver (CDW)", "YES", "YES", "YES"))
print("{:<45}{:^25}{:^25}{:^25}".format("Driver + Passenger Injury Insurance (PAI)", "YES", "YES", "YES"))
print("{:<45}{:^25}{:^25}{:^25}".format("Third Party Insurance (TP)", "YES", "YES", "YES"))
print("{:<45}{:^26}{:^24}{:^25}".format("Super Collision Damage Waiver (SCDW)", "NO", "YES", "YES"))
print("{:<45}{:^26}{:^24}{:^25}".format("Windshield Insurance (GP)", "NO", "YES", "YES"))
print("{:<45}{:^26}{:^25}{:^24}".format("Sand And Dust Waiver (SADW)", "NO", "NO", "YES"))
print("{:<45}{:^26}{:^25}{:^24}".format("No Deductable Insurance (ZERO)", "NO", "NO", "YES"))

print()
print()

print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance price per day:", "Small Car", "Family Car", "Van", "SUV"))
print("-" * 140)
print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance Package 1", "2.000kr", "2.000kr", "3.750kr", "3.300kr"))
print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance package 2", "3.750kr", "3.750kr", "6.000kr", "5.500kr"))
print()
print()
print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Max Deductable Insurance:", "Small Car", "Family Car", "Van", "SUV"))
print("-" * 140)
print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Included Insurance", "195.000kr", "195.000kr", "395.000kr", "375.000kr"))
print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance Package 1", "49.500kr", "49.500kr", "105.000kr", "95.000kr"))
print("{:<45}{:^25}{:^25}{:^25}{:^25}".format("Insurance package 2", "0kr", "0kr", "0kr", "0kr"))
_ = input()
