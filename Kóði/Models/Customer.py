class Customer:

    def __init__(self, name, soc_sec_num, home_address, local_address, 
        phone_num, email, driv_license, card_num):
        self.__name = name
        self.__soc_sec_num = soc_sec_num
        self.__home_address = home_address
        self.__local_address = local_address
        self.__phone_num = phone_num
        self.__email = email
        self.__driv_license = driv_license
        self.__card_num = card_num

    def get_name(self):
        return self.__name

    def get_soc_sec_num(self):
        return self.__soc_sec_num
    
    def get_home_address(self):
        return self.__home_address

    def get_local_address(self):
        return self.__local_address

    def get_phone_num(self):
        return self.__phone_num

    def get_email(self):
        return self.__email

    def get_driv_license(self):
        return self.__driv_license

    def get_card_num(self):
        return self.__card_num

    def set_name(self, name):
        self.__name = name
    
    def set_home_address(self, home_address):
        self.__home_address = home_address

    def set_local_address(self, local_address):
        self.__local_address = local_address

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def set_email(self, email):
        self.__email = email

    def set_driv_license(self, driv_license):
        self.__driv_license = driv_license

    def set_card_num(self, card_num):
        self.__card_num = card_num

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.__name, self.__soc_sec_num, 
            self.__home_address, self.__local_address, self.__phone_num, self.__email, 
            self.__driv_license, self.__card_num)