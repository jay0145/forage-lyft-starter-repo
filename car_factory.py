from abc import ABC, abstractmethod
import datetime
import sys
sys.path.append(r"C:\My Files\Projects\Lyft V-Internship\forage-lyft-starter-repo\engine")
sys.path.append(r"C:\My Files\Projects\Lyft V-Internship\forage-lyft-starter-repo\battery")
sys.path.append(r"C:\My Files\Projects\Lyft V-Internship\forage-lyft-starter-repo")
from engine import engine 
from battery import battery
from car import Car
        
class car_factory():
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = Car()
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        last_service_date = datetime.datetime.strptime(last_service_date, "%Y-%m-%d")
        calliope.car_battery = battery.spindler_battery(current_date, last_service_date)
        calliope.car_engine = engine.capulet_engine(current_mileage, last_service_mileage)
        return calliope
        
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = Car()
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        last_service_date = datetime.datetime.strptime(last_service_date, "%Y-%m-%d")
        glissade.car_battery = battery.spindler_battery(current_date, last_service_date)
        glissade.car_engine = engine.willoughby_engine(current_mileage, last_service_mileage)
        return glissade
    
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        palindrome = Car()
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        last_service_date = datetime.datetime.strptime(last_service_date, "%Y-%m-%d")
        palindrome.car_battery = battery.spindler_battery(current_date, last_service_date)
        palindrome.car_engine = engine.sternman_engine(warning_light_is_on)
        return palindrome
        
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = Car()
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        last_service_date = datetime.datetime.strptime(last_service_date, "%Y-%m-%d")
        rorschach.car_battery = battery.nubbin_battery(current_date, last_service_date)
        rorschach.car_engine = engine.willoughby_engine(current_mileage, last_service_mileage)
        return rorschach
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = Car()
        current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        last_service_date = datetime.datetime.strptime(last_service_date, "%Y-%m-%d")
        thovex.car_battery = battery.nubbin_battery(current_date, last_service_date)
        thovex.car_engine = engine.capulet_engine(current_mileage, last_service_mileage)
        return thovex
    
    
    
    
    
        