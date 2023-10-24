from tires.tires import tires

class CarriganTires(tires):
    def __init__(self, tire_wear_list):
        super().__init__(tire_wear_list)
    def needs_service(self):
        for tire in self.tire_wear_list:
            if tire >= 0.9:
                return True
        return False
