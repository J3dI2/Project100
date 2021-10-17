class atm(object):
    def __init__(self, CashWithdrawl, BalanceEnquiry):
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def cash_taken(self):
        print("processing...")
        "Withdrawl amount here"

    def balance(self):
        print("caluating...")
        "Amount of cash in bank account here"