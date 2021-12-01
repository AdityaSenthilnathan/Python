class Car (object):
    def __init__(self, speed, cost):
        self.speed = speed
        self.cost = cost

    def GetCost(self):
        print(self.cost)

    def GetSpeed(self):
        print(self.speed)

Car1 = Car("12kmph", "$1200" )
Car2 = Car("10kmph", "$800" )

print(Car2.speed)