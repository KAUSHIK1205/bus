class vehicle:
    def __init__(self,mileage,model):
        self.mileage=mileage
        self.model=model

class bus(vehicle):
    def car(self,mileage,model):
        pass

obj=bus("12 m/p h","VOLVO(branded)")

print(obj.mileage,obj.model)