import unittest
import sys
sys.path.append(r'C:\My Files\Projects\Lyft V-Internship\forage_lyft_starter_repo_jay')#kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    
    def test_tire_should_be_serviced(self):
        tires = OctoprimeTires([0.9,0.6,0.9,0.6])
        self.assertTrue(tires.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        tires = OctoprimeTires([0.5,0.5,0.5,0.5])
        self.assertFalse(tires.needs_service())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

