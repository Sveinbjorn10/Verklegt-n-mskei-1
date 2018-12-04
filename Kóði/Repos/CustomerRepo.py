from Models.Customer import Customer

class CustomerRepo:
    def __init__(self):
        self.__customers = []

    def add_customer(self, customer):
        # first add to file then to private list
        with open("./data/customer.csv", "a+") as customer_file:
            name = customer.get_name()
            soc_sec_num = customer.get_soc_sec_num()
            home_address = customer.get_home_address()
            local_address = customer.get_local_address()
            phone_num = customer.get_phone_num()
            email = customer.get_email()
            driv_license = customer.get_driv_license()
            card_num = customer.get_card_num()
            customer_file.write("{},{},{},{},{},{},{},{}\n".format(name, soc_sec_num, 
                home_address, local_address, phone_num, email, driv_license, card_num))

    def get_customer(self):
        if self.__customers == []:
            with open("./data/customers.csv", "r") as customer_file:
                for line in customer_file.readlines():
                    name, soc_sec_num, home_address, local_address, phone_num, email, driv_license, 
                        card_num = line.split(",")
                    new_customer = Customer(name, soc_sec_num, home_address, local_address, phone_num, email, 
                        driv_license, card_num)
                    self.__customers.append(new_customer)    
        return self.__customers