class Car:
    def __init__(self,engine,torque):
        self.engine=engine
        self.torque=torque
    
    def accelerator(self):
        print(self.name+"is accelerating")
swift=Car(1197,250)
fortuner=Car(2018,250)
print(swift.engine,swift.torque)