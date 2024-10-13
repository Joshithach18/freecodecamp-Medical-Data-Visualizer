# test_module.py

import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):
    def test_cat_plot(self):
        """Test that the categorical plot returns a figure."""
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)

    def test_heat_map(self):
        """Test that the heat map returns a figure."""
        fig = draw_heat_map()
        self.assertIsNotNone(fig)

def run_tests():
    unittest.main(exit=False)
