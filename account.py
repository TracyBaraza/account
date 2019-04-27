class Account:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.balance = 0






    

        

    def welcome(self):
        return "Hello {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


    def deposit(self,y):
        deposit = y
        self.deposits.append(y)
        
        self.balance = self.balance + y

        dps = "Dear {} {} deposit of kes {} was successful current balance is {}".format(self.first_name,self.last_name,y,self.balance)
        return dps


    def show_deposits(self):
        for y in self.deposits:
            print(y)
        

    def withdraw(self,x):
        withdraw = x

        self.withdrawals.append(x)


        if x>self.balance:
            return "cant withdraw"
        else:
            self.balance = self.balance - x



            


            msg = "Dear {} {} withdrawal of kes {} was successful current balance is {}".format(self.first_name,self.last_name,x,self.balance)
            return msg


    def show_withdrawals(self):
        for x in self.withdrawals:
            print(x)
    

    def show_balance(self):
        show_balance = self.balance
        text = "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
        return text



    def give_loan(self,c):
         loan = c

         if len(self.deposits)>=5 and c<sum(self.deposits) and c<(1/3*sum(self.deposits)) and self.loan==0:
            self.loan = self.loan + c
            print("Dear customer your loan of {} has been approved".format(c))



    def repay_loan(self,d):
        payment = d

        self.loan.extend(d)

        self.loan = self.loan-d
        excess_payment = self.deposit.append(deposit)

        loanm = "Dear customer you have paid kes {} your remaining loan balance is now {}".format(d,self.loan)
        print(loanm)


       