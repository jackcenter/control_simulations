from tractor_trailer.models.tractor_trailer_plant import (
    TractorTrailerPlant,
    TractorTrailerPlantOptions,
)

import math
import unittest

from tractor_trailer.custom_types.tractor_input import TractorInput
from tractor_trailer.custom_types.tractor_trailer_state import TractorTrailerState


class TestTractorTrailerPlant(unittest.TestCase):
    def test_construction(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)

    def test_simulate_parked(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)
        
        initial_tractor_trailer_state = TractorTrailerState(
            x_ordinate=0.0,
            y_ordinate=0.0,
            heading_rad=0.0,
            velocity_mps=0.0,
            steering_angle_rad=0.0,
            trailer_heading_rad=0.0,
        )
        
        tractor_input = TractorInput(
            acceleration_mpss=0.0,
            steering_rate_rps=0.0
        )
        
        tractor_trailer_state = tractor_trailer_plant.simulate(initial_tractor_trailer_state, tractor_input, 1.0)
        self.assertEqual(initial_tractor_trailer_state, tractor_trailer_state)
        
    def test_simulate_driving_straight_east(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)
        
        initial_tractor_trailer_state = TractorTrailerState(
            x_ordinate=0.0,
            y_ordinate=0.0,
            heading_rad=0.0,
            velocity_mps=1.0,
            steering_angle_rad=0.0,
            trailer_heading_rad=0.0,
        )
        
        tractor_input = TractorInput(
            acceleration_mpss=0.0,
            steering_rate_rps=0.0
        )
        
        tractor_trailer_state = tractor_trailer_plant.simulate(initial_tractor_trailer_state, tractor_input, 1.0)
        self.assertAlmostEqual(1.0, tractor_trailer_state.x_ordinate)
        self.assertAlmostEqual(0.0, tractor_trailer_state.y_ordinate)
        self.assertAlmostEqual(0.0, tractor_trailer_state.heading_rad)
        self.assertAlmostEqual(1.0, tractor_trailer_state.velocity_mps)
        self.assertAlmostEqual(0.0, tractor_trailer_state.steering_angle_rad)
        self.assertAlmostEqual(0.0, tractor_trailer_state.trailer_heading_rad)
    
    def test_simulate_driving_straight_west(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)
        
        initial_tractor_trailer_state = TractorTrailerState(
            x_ordinate=0.0,
            y_ordinate=0.0,
            heading_rad=math.pi / 2.0,
            velocity_mps=1.0,
            steering_angle_rad=0.0,
            trailer_heading_rad=math.pi / 2.0,
        )
        
        tractor_input = TractorInput(
            acceleration_mpss=0.0,
            steering_rate_rps=0.0
        )
        
        tractor_trailer_state = tractor_trailer_plant.simulate(initial_tractor_trailer_state, tractor_input, 1.0)
        self.assertAlmostEqual(0.0, tractor_trailer_state.x_ordinate)
        self.assertAlmostEqual(1.0, tractor_trailer_state.y_ordinate)
        self.assertAlmostEqual(math.pi / 2.0, tractor_trailer_state.heading_rad)
        self.assertAlmostEqual(1.0, tractor_trailer_state.velocity_mps)
        self.assertAlmostEqual(0.0, tractor_trailer_state.steering_angle_rad)
        self.assertAlmostEqual(math.pi / 2.0, tractor_trailer_state.trailer_heading_rad)
        
    def test_simulate_turning(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)
        
        initial_tractor_trailer_state = TractorTrailerState(
            x_ordinate=0.0,
            y_ordinate=0.0,
            heading_rad=0.0,
            velocity_mps=1.0,
            steering_angle_rad=math.pi / 4.0,
            trailer_heading_rad=0.0,
        )
        
        tractor_input = TractorInput(
            acceleration_mpss=0.0,
            steering_rate_rps=0.0
        )
        
        tractor_trailer_state = tractor_trailer_plant.simulate(initial_tractor_trailer_state, tractor_input, 1.0)
        self.assertAlmostEqual(1.0, tractor_trailer_state.heading_rad)
        self.assertGreater(tractor_trailer_state.trailer_heading_rad, 0.0)
        
    def test_simulate_acceleration_input(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)
        
        initial_tractor_trailer_state = TractorTrailerState(
            x_ordinate=0.0,
            y_ordinate=0.0,
            heading_rad=0.0,
            velocity_mps=0.0,
            steering_angle_rad=0.0,
            trailer_heading_rad=0.0,
        )
        
        tractor_input = TractorInput(
            acceleration_mpss=1.0,
            steering_rate_rps=0.0
        )
        
        tractor_trailer_state = tractor_trailer_plant.simulate(initial_tractor_trailer_state, tractor_input, 1.0)
        self.assertAlmostEqual(1.0, tractor_trailer_state.velocity_mps)
        
    def test_simulate_steering_rate_input(self):
        tractor_trailer_plant_options = TractorTrailerPlantOptions(
            wheel_base_m=1.0, bogey_distance_m=2.0
        )
        tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)
        
        initial_tractor_trailer_state = TractorTrailerState(
            x_ordinate=0.0,
            y_ordinate=0.0,
            heading_rad=0.0,
            velocity_mps=1.0,
            steering_angle_rad=0.0,
            trailer_heading_rad=0.0,
        )
        
        tractor_input = TractorInput(
            acceleration_mpss=0.0,
            steering_rate_rps=1.0
        )
        
        tractor_trailer_state = tractor_trailer_plant.simulate(initial_tractor_trailer_state, tractor_input, 1.0)
        self.assertAlmostEqual(1.0, tractor_trailer_state.steering_angle_rad)
        