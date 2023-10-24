import unittest
import sys
sys.path.append(r'C:\My Files\Projects\Lyft V-Internship\forage_lyft_starter_repo_jay')
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    
    def test_tire_should_be_serviced(self):
        tires = CarriganTires([0.9,0.1,0.1,0.1])
        self.assertTrue(tires.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        tires = CarriganTires([0.8,0.8,0.8,0.8])
        self.assertFalse(tires.needs_service())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
