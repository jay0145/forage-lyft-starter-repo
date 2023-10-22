from abc import ABC, abstractmethod


class Car():
    def __init__(self):
        self.car_engine = None
        self.car_battery = None

    def needs_service(self):
        pass
