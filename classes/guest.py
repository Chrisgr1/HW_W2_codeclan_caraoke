class Guest:

    def __init__(self, f_name, l_name, wallet):
        self.f_name = f_name
        self.l_name = l_name
        self.wallet = wallet

    def pay_to_check_in(self, amount):
        self.wallet -= amount