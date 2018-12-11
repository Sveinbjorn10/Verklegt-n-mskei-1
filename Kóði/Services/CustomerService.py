from Repos.CustomerRepo import CustomerRepo

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()

    def print_customer_database(self):
        print(self.__customer_repo)