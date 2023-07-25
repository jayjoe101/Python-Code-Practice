from car import Car

class Traffic():

    def __init__(self):
        self.traffic = []

    def add_car(self):
        self.traffic.append(Car())

    def create_traffic(self, level):
        for _ in range(level*5):
            self.add_car()

    def clear_traffic(self):
        for car in self.traffic:
            car.delete()