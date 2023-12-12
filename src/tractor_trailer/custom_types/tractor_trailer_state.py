from typing import List

import numpy as np


class TractorTrailerState:
    def __init__(
        self,
        x_ordinate: float = 0.0,
        y_ordinate: float = 0.0,
        heading_rad: float = 0.0,
        velocity_mps: float = 0.0,
        steering_angle_rad: float = 0.0,
        trailer_heading_rad: float = 0.0,
    ) -> None:
        self.x_ordinate = x_ordinate
        self.y_ordinate = y_ordinate
        self.heading_rad = heading_rad
        self.velocity_mps = velocity_mps
        self.steering_angle_rad = steering_angle_rad
        self.trailer_heading_rad = trailer_heading_rad

    def __eq__(self, other):
        if isinstance(other, TractorTrailerState):
            return (
                self.x_ordinate,
                self.y_ordinate,
                self.heading_rad,
                self.velocity_mps,
                self.steering_angle_rad,
                self.trailer_heading_rad,
            ) == (
                other.x_ordinate,
                other.y_ordinate,
                other.heading_rad,
                other.velocity_mps,
                other.steering_angle_rad,
                other.trailer_heading_rad,
            )

        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __repr__(self):
        return " TractorTrailerState: {}\n".format(self.get_list())

    def __str__(self):
        return (
            "x_ordinate:\t\t{x}\n"
            "y_ordinate:\t\t{y}\n"
            "heading_rad:\t\t{heading}\n"
            "velocity_mps:\t\t{velocity}\n"
            "steering_angle_rad:\t{steering}\n"
            "trailer_heading_rad:\t{trailer}\n".format(
                x=self.x_ordinate,
                y=self.y_ordinate,
                heading=self.heading_rad,
                velocity=self.velocity_mps,
                steering=self.steering_angle_rad,
                trailer=self.trailer_heading_rad,
            )
        )

    def get_array(self) -> np.ndarray:
        """
        Returns a one dimensional numpy array of the class fields.
        """
        return np.array(
            [
                self.x_ordinate,
                self.y_ordinate,
                self.heading_rad,
                self.velocity_mps,
                self.steering_angle_rad,
                self.trailer_heading_rad,
            ]
        )

    def get_list(self) -> List[float]:
        """
        Returns a list of the class fields.
        """
        return [
            self.x_ordinate,
            self.y_ordinate,
            self.heading_rad,
            self.velocity_mps,
            self.steering_angle_rad,
            self.trailer_heading_rad,
        ]

    def get_vector(self) -> np.ndarray:
        """
        Returns a two dimensional numpy array of the class fields as a vector
        """
        return np.array(
            [
                [self.x_ordinate],
                [self.y_ordinate],
                [self.heading_rad],
                [self.velocity_mps],
                [self.steering_angle_rad],
                [self.trailer_heading_rad],
            ]
        )

    @staticmethod
    def create_from_array(array: np.ndarray):
        """
        Returns a TractorTrailerState from a numpy array of state values.
        """
        return TractorTrailerState(
            x_ordinate=array[0],
            y_ordinate=array[1],
            heading_rad=array[2],
            velocity_mps=array[3],
            steering_angle_rad=array[4],
            trailer_heading_rad=array[5],
        )

    @staticmethod
    def create_from_list(list: List[float]):
        """
        Returns a TractorTrailerState from a list of state values.
        """
        return TractorTrailerState(
            x_ordinate=list[0],
            y_ordinate=list[1],
            heading_rad=list[2],
            velocity_mps=list[3],
            steering_angle_rad=list[4],
            trailer_heading_rad=list[5],
        )

    @staticmethod
    def create_from_vector(vector: np.ndarray):
        """
        Returns a TractorTrailerState from a vector of state values represented by a two dimensional numpy array.
        """
        return TractorTrailerState(
            x_ordinate=vector[0][0],
            y_ordinate=vector[1][0],
            heading_rad=vector[2][0],
            velocity_mps=vector[3][0],
            steering_angle_rad=vector[4][0],
            trailer_heading_rad=vector[5][0],
        )
