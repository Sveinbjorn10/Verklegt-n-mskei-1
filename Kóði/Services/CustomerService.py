from repos.CustomerRepo import CustomerRepo

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepo()