def titles():
    print("{:<33s}{:<33s}{:<21}{:<21}{:<21}".format("Car kind", "Car type", "Price per day", "HEllo", "Sælir"))
    print("-" * 130)

def smallcars():
    print("{:<33s}{:<33s}{:<21}".format("Small Cars", "VW Golf", "11.260"))
    print("{:<33s}{:<33s}{:<21}".format("", "Hyundai i10", "9.265"))
    print("")

def familycars():
    print("{:<33s}{:<33s}{:<21}".format("Family Cars", "Toyota Corolla", "13.775"))
    print("{:<33s}{:<33s}{:<21}".format("", "Skoda Octavia", "15.675"))
    print("")

def suv():
    print("{:<33s}{:<33s}{:<21}".format("Suvs", "Audi Q5", "27.885"))
    print("{:<33s}{:<33s}{:<21}".format("", "Toyota Landcruiser", "29.355"))
    print("{:<33s}{:<33s}{:<21}".format("", "Toyota Rav4", "20.000"))
    print("")

def van():
    print("{:<33s}{:<33s}{:<21}".format("Vans", "Ford Galaxy", "18.480"))
    print("{:<33s}{:<33s}{:<21}".format("", "Renault Traffic3", "27.165"))
    print("{:<33s}{:<33s}{:<21}".format("", "VW Caravelle 4wd", "28.595"))
    print("")

def sendvan():
    print("{:<33s}{:<33s}{:<21}".format("Vans", "Ford Transit (14 seats)", "41.500"))
    print("{:<33s}{:<33s}{:<21}".format("", "Mercedes Sprinter (15 seats)", "45.700"))
    print("")


def main():
    titles()
    smallcars()
    familycars()
    suv()
    van()
    sendvan()

main()