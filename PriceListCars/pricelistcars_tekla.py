def titles():
    print("{:<33s}{:<33s}{:<21}".format("Car class", "Price per day", "Car make e.g"))
    print("-" * 100)

def smallcars():
    print("{:<33s}{:<33s}{:<21}".format("Small Car", "10.000kr", "VW Golf"))
    print("{:<33s}{:<33s}{:<21}".format("", "", "Hyundai i10"))
    print("")

def familycars():
    print("{:<33s}{:<33s}{:<21}".format("Family Car", "14.000kr", "Toyota Corolla"))
    print("{:<33s}{:<33s}{:<21}".format("", "", "Skoda Octavia"))
    print("")

def van():
    print("{:<33s}{:<33s}{:<21}".format("Van", "25.000kr", "Ford Galaxy"))
    print("{:<33s}{:<33s}{:<21}".format("", "", "Renault Traffic3"))
    print("{:<33s}{:<33s}{:<21}".format("", "", "VW Caravelle 4wd"))
    print("")

def suv():
    print("{:<33s}{:<33s}{:<21}".format("Suv", "20.000kr", "Audi Q5"))
    print("{:<33s}{:<33s}{:<21}".format("", "", "Toyota Landcruiser"))
    print("{:<33s}{:<33s}{:<21}".format("", "", "Toyota Rav4"))
    print("")


def main():
    titles()
    smallcars()
    familycars()
    van()
    suv()

main()