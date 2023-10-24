from abc import ABC
import datetime

class Battery():
    def needs_service():
        pass
    
class spindler_battery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        self.current_date = datetime.datetime.now()
        difference = self.current_date - self.last_service_date
        unserviced_period = difference.days
        if unserviced_period > 1095: #3 years
            return True
        else:
            return False

class nubbin_battery(Battery):
    
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        pass
        self.current_date = datetime.datetime.now()
        difference = self.current_date - self.last_service_date
        unserviced_period = difference.days
        if unserviced_period > 1460: #4 years
            return True
        else:
            return False