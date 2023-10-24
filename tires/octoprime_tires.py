from tires.tires import tires

class OctoprimeTires(tires):
    def __init__(self, tire_wear_list):
        super().__init__(tire_wear_list)
    def needs_service(self):
        total_wear = 0
        for tire in self.tire_wear_list:
            total_wear += tire
        if total_wear >= 3:
            return True
        else:
            return False
