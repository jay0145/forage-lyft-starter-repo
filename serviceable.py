from car import Car
from car_factory import car_factory
class Serviceable(Car):
    def needs_service(car):
        if car.car_engine.needs_service or car.car_battery.needs_service:
            return True
        else:
            return False