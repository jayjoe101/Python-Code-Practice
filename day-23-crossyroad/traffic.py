from car import Car

class Traffic():

    def __init__(self):
        self.traffic = []

    def add_car(self):
        self.traffic.append(Car())

    def create_traffic(self, level, speed=1):
        for n in range(level*5):
            self.add_car()
            self.traffic[n].car_speed = speed

    def clear_traffic(self):
        for car in self.traffic:
            car.goto(1000,1000)
        self.traffic = []