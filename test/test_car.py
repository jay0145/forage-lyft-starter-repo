import unittest
from datetime import datetime
import sys
sys.path.append(r'C:\My Files\Projects\Lyft V-Internship\forage_lyft_starter_repo_jay')
from engine.engine import capulet_engine
from engine.engine import willoughby_engine
from engine.engine import sternman_engine

from battery.battery import spindler_battery
from battery.battery import nubbin_battery

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)
        
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)
        
        self.assertFalse(engine.needs_service())
        
class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = sternman_engine(warning_light_is_on)
        
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = sternman_engine(warning_light_is_on)
        
        self.assertFalse(engine.needs_service())
        
class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = spindler_battery(current_date, last_service_date)
        
        self.assertTrue(battery.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = spindler_battery(current_date, last_service_date)
        
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = nubbin_battery(current_date, last_service_date)
        
        self.assertTrue(battery.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=current_date.year - 2)
        battery = nubbin_battery(current_date, last_service_date)
        
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main(verbosity=2)
