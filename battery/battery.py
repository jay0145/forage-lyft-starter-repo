from abc import ABC
import datetime

class battery():
    def needs_service():
        pass
    
class spindler_battery(battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service():
        self.current_date = datetime.datetime.now()
        difference = self.current_date - self.last_service_date
        unserviced_period = difference.days
        if unserviced_period >= 730:
            return True
        else:
            return False

class nubbin_battery(battery):
    
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service():
        self.current_date = datetime.datetime.now()
        difference = self.current_date - self.last_service_date
        unserviced_period = difference.days
        if unserviced_period >= 1460:
            return True
        else:
            return False