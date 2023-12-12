from tractor_trailer.custom_types.tractor_trailer_state import TractorTrailerState

import unittest

import numpy as np


class TestTractorTrailerState(unittest.TestCase):
    def test_construction(self):
        tractor_trailer_state = TractorTrailerState()

        self.assertEqual(0.0, tractor_trailer_state.x_ordinate)
        self.assertEqual(0.0, tractor_trailer_state.y_ordinate)
        self.assertEqual(0.0, tractor_trailer_state.heading_rad)
        self.assertEqual(0.0, tractor_trailer_state.velocity_mps)
        self.assertEqual(0.0, tractor_trailer_state.steering_angle_rad)
        self.assertEqual(0.0, tractor_trailer_state.trailer_heading_rad)

    def test_get_array(self):
        x_ordinate = 0.1
        y_ordinate = 1.2
        heading_rad = 2.3
        velocity_mps = 3.4
        steering_angle_rad = 4.5
        trailer_heading_rad = 5.6

        tractor_trailer_state = TractorTrailerState(
            x_ordinate=x_ordinate,
            y_ordinate=y_ordinate,
            heading_rad=heading_rad,
            velocity_mps=velocity_mps,
            steering_angle_rad=steering_angle_rad,
            trailer_heading_rad=trailer_heading_rad,
        )

        expected_tractor_trailer_state_array = np.array(
            [
                x_ordinate,
                y_ordinate,
                heading_rad,
                velocity_mps,
                steering_angle_rad,
                trailer_heading_rad,
            ]
        )

        tractor_trailer_state_array = tractor_trailer_state.get_array()
        self.assertIsInstance(tractor_trailer_state_array, np.ndarray)
        self.assertTrue(
            np.array_equal(
                expected_tractor_trailer_state_array, tractor_trailer_state_array
            )
        )

    def test_get_list(self):
        x_ordinate = 0.1
        y_ordinate = 1.2
        heading_rad = 2.3
        velocity_mps = 3.4
        steering_angle_rad = 4.5
        trailer_heading_rad = 5.6

        tractor_trailer_state = TractorTrailerState(
            x_ordinate=x_ordinate,
            y_ordinate=y_ordinate,
            heading_rad=heading_rad,
            velocity_mps=velocity_mps,
            steering_angle_rad=steering_angle_rad,
            trailer_heading_rad=trailer_heading_rad,
        )

        expected_tractor_trailer_state_list = [
            x_ordinate,
            y_ordinate,
            heading_rad,
            velocity_mps,
            steering_angle_rad,
            trailer_heading_rad,
        ]

        tractor_trailer_state_list = tractor_trailer_state.get_list()
        self.assertIsInstance(tractor_trailer_state_list, list)
        self.assertTrue(expected_tractor_trailer_state_list, tractor_trailer_state_list)

    def test_get_vector(self):
        x_ordinate = 0.1
        y_ordinate = 1.2
        heading_rad = 2.3
        velocity_mps = 3.4
        steering_angle_rad = 4.5
        trailer_heading_rad = 5.6

        tractor_trailer_state = TractorTrailerState(
            x_ordinate=x_ordinate,
            y_ordinate=y_ordinate,
            heading_rad=heading_rad,
            velocity_mps=velocity_mps,
            steering_angle_rad=steering_angle_rad,
            trailer_heading_rad=trailer_heading_rad,
        )

        expected_tractor_trailer_state_vector = np.array(
            [
                [x_ordinate],
                [y_ordinate],
                [heading_rad],
                [velocity_mps],
                [steering_angle_rad],
                [trailer_heading_rad],
            ]
        )

        tractor_trailer_state_vector = tractor_trailer_state.get_vector()
        self.assertIsInstance(tractor_trailer_state_vector, np.ndarray)
        self.assertTrue(
            np.array_equal(
                expected_tractor_trailer_state_vector, tractor_trailer_state_vector
            )
        )

    def test_create_from_array(self):
        x_ordinate = 0.1
        y_ordinate = 1.2
        heading_rad = 2.3
        velocity_mps = 3.4
        steering_angle_rad = 4.5
        trailer_heading_rad = 5.6

        expected_tractor_trailer_state = TractorTrailerState(
            x_ordinate=x_ordinate,
            y_ordinate=y_ordinate,
            heading_rad=heading_rad,
            velocity_mps=velocity_mps,
            steering_angle_rad=steering_angle_rad,
            trailer_heading_rad=trailer_heading_rad,
        )

        tractor_trailer_state_array = np.array(
            [
                x_ordinate,
                y_ordinate,
                heading_rad,
                velocity_mps,
                steering_angle_rad,
                trailer_heading_rad,
            ]
        )

        self.assertEqual(
            expected_tractor_trailer_state,
            TractorTrailerState.create_from_array(tractor_trailer_state_array),
        )

    def test_create_from_list(self):
        x_ordinate = 0.1
        y_ordinate = 1.2
        heading_rad = 2.3
        velocity_mps = 3.4
        steering_angle_rad = 4.5
        trailer_heading_rad = 5.6

        expected_tractor_trailer_state = TractorTrailerState(
            x_ordinate=x_ordinate,
            y_ordinate=y_ordinate,
            heading_rad=heading_rad,
            velocity_mps=velocity_mps,
            steering_angle_rad=steering_angle_rad,
            trailer_heading_rad=trailer_heading_rad,
        )

        tractor_trailer_state_list = [
            x_ordinate,
            y_ordinate,
            heading_rad,
            velocity_mps,
            steering_angle_rad,
            trailer_heading_rad,
        ]

        self.assertEqual(
            expected_tractor_trailer_state,
            TractorTrailerState.create_from_list(tractor_trailer_state_list),
        )

    def test_create_from_vector(self):
        x_ordinate = 0.1
        y_ordinate = 1.2
        heading_rad = 2.3
        velocity_mps = 3.4
        steering_angle_rad = 4.5
        trailer_heading_rad = 5.6

        expected_tractor_trailer_state = TractorTrailerState(
            x_ordinate=x_ordinate,
            y_ordinate=y_ordinate,
            heading_rad=heading_rad,
            velocity_mps=velocity_mps,
            steering_angle_rad=steering_angle_rad,
            trailer_heading_rad=trailer_heading_rad,
        )

        tractor_trailer_state_vector = np.array(
            [
                [x_ordinate],
                [y_ordinate],
                [heading_rad],
                [velocity_mps],
                [steering_angle_rad],
                [trailer_heading_rad],
            ]
        )

        self.assertEqual(
            expected_tractor_trailer_state,
            TractorTrailerState.create_from_vector(tractor_trailer_state_vector),
        )
