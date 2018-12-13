def titles():
    print("{:<33s}{:<33s}{:<21}{:<21}{:<21}".format("Car kind", "Car type", "Price per day", "HEllo", "Sælir"))
    print("-" * 130)

def smallcars():
    print("{:<33s}{:<33s}{:<21}".format("Small Cars", "VW Golf", "11.260"))
    print("{:<33s}{:<33s}{:<21}\n".format("", "Hyundai i10", "9.265"))

def familycars():
    print("{:<33s}{:<33s}{:<21}".format("Family Cars", "Toyota Corolla", "13.775"))
    print("{:<33s}{:<33s}{:<21}\n".format("", "Skoda Octavia", "15.675"))

def suv():
    print("{:<33s}{:<33s}{:<21}".format("Suvs", "Audi Q5", "27.885"))
    print("{:<33s}{:<33s}{:<21}".format("", "Toyota Landcruiser", "29.355"))
    print("{:<33s}{:<33s}{:<21}\n".format("", "Toyota Rav4", "20.000"))

def van():
    print("{:<33s}{:<33s}{:<21}".format("Vans", "Ford Galaxy", "18.480"))
    print("{:<33s}{:<33s}{:<21}".format("", "Renault Traffic3", "27.165"))
    print("{:<33s}{:<33s}{:<21}\n".format("", "VW Caravelle 4wd", "28.595"))

def sendvan():
    print("{:<33s}{:<33s}{:<21}".format("Vans", "Ford Transit (14 seats)", "41.500"))
    print("{:<33s}{:<33s}{:<21}\n".format("", "Mercedes Sprinter (15 seats)", "45.700"))


def main():
    titles()
    smallcars()
    familycars()
    suv()
    van()
    sendvan()

main()