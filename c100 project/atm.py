class Atm(object):
    def __init__(self,account_number,card_number,pin):
        self.account_number=account_number
        self.number=card_number
        self.pin=pin
       

    def get_pin(self):
        print(self.pin)


Samanyu=Atm("9611550306","298578152","season2 hip_hop_bundle")
print(Samanyu.pin)
