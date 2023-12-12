from tractor_trailer.custom_types.tractor_input import TractorInput

import unittest

import numpy as np


class TestTractorInput(unittest.TestCase):
    def test_construction(self):
        tractor_input = TractorInput()

        self.assertEqual(0.0, tractor_input.acceleration_mpss)
        self.assertEqual(0.0, tractor_input.steering_rate_rps)

    def test_get_array(self):
        acceleration_mpss = 0.1
        steering_rate_rps = 1.2

        tractor_input = TractorInput(
            acceleration_mpss=acceleration_mpss, steering_rate_rps=steering_rate_rps
        )

        expected_tractor_input_array = np.array([acceleration_mpss, steering_rate_rps])

        tractor_input_array = tractor_input.get_array()
        self.assertIsInstance(tractor_input_array, np.ndarray)
        self.assertTrue(
            np.array_equal(expected_tractor_input_array, tractor_input_array)
        )

    def test_get_list(self):
        acceleration_mpss = 0.1
        steering_rate_rps = 1.2

        tractor_input = TractorInput(
            acceleration_mpss=acceleration_mpss, steering_rate_rps=steering_rate_rps
        )

        expected_tractor_input_list = [acceleration_mpss, steering_rate_rps]

        tractor_input_list = tractor_input.get_list()
        self.assertIsInstance(tractor_input_list, list)
        self.assertEqual(expected_tractor_input_list, tractor_input_list)

    def test_get_vector(self):
        acceleration_mpss = 0.1
        steering_rate_rps = 1.2

        tractor_input = TractorInput(
            acceleration_mpss=acceleration_mpss, steering_rate_rps=steering_rate_rps
        )

        expected_tractor_input_array = np.array(
            [[acceleration_mpss], [steering_rate_rps]]
        )

        tractor_input_vector = tractor_input.get_vector()
        self.assertIsInstance(tractor_input_vector, np.ndarray)
        self.assertTrue(
            np.array_equal(expected_tractor_input_array, tractor_input_vector)
        )

    def test_create_from_array(self):
        acceleration_mpss = 0.1
        steering_rate_rps = 1.2

        expected_tractor_input = TractorInput(
            acceleration_mpss=acceleration_mpss, steering_rate_rps=steering_rate_rps
        )

        tractor_input_array = np.array([acceleration_mpss, steering_rate_rps])

        self.assertEqual(
            expected_tractor_input,
            TractorInput.create_from_array(tractor_input_array),
        )

    def test_create_from_list(self):
        acceleration_mpss = 0.1
        steering_rate_rps = 1.2

        expected_tractor_input = TractorInput(
            acceleration_mpss=acceleration_mpss, steering_rate_rps=steering_rate_rps
        )

        tractor_input_list = [acceleration_mpss, steering_rate_rps]

        self.assertEqual(
            expected_tractor_input,
            TractorInput.create_from_list(tractor_input_list),
        )

    def test_create_from_vector(self):
        acceleration_mpss = 0.1
        steering_rate_rps = 1.2

        expected_tractor_input = TractorInput(
            acceleration_mpss=acceleration_mpss, steering_rate_rps=steering_rate_rps
        )

        tractor_input_vector = np.array([[acceleration_mpss], [steering_rate_rps]])

        self.assertEqual(
            expected_tractor_input,
            TractorInput.create_from_vector(tractor_input_vector),
        )
