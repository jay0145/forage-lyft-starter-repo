from abc import ABC

#interface
class engine():
    def needs_service():
        pass
    
class capulet_engine(engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    
class willoughby_engine(engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
    
class sternman_engine(engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
        
    def needs_service(self):
        return warning_light_is_on
        