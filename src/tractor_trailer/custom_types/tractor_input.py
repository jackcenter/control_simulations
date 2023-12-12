from typing import List

import numpy as np

class TractorInput:
    def __init__(
        self, acceleration_mpss: float = 0.0, steering_rate_rps: float = 0.0
    ) -> None:
        self.acceleration_mpss = acceleration_mpss
        self.steering_rate_rps = steering_rate_rps

    def __eq__(self, other):
        if isinstance(other, TractorInput):
            return (self.acceleration_mpss, self.steering_rate_rps) == (
                other.acceleration_mpss,
                other.steering_rate_rps,
            )
            
        return NotImplemented
        
    def __ne__(self, other):
        result = self.__eq__(other)  
        if result is NotImplemented:  
            return result  
        return not result 

    def __repr__(self):
        return " TractorInput: {}\n".format(self.get_list())
        
    def __str__(self):
        return (
            "acceleration_mpss:\t{acceleration}\n"
            "steering_rate_rps:\t{steering}\n".format(
                acceleration=self.acceleration_mpss,
                steering=self.steering_rate_rps
            )
        )
        
    def get_array(self) -> np.ndarray:
        """
        Returns a one dimensional numpy array of the class fields.
        """
        return np.array(
            [
                self.acceleration_mpss,
                self.steering_rate_rps
            ]
        )
    
    def get_list(self) -> List[float]:
        """
        Returns a list of the class fields.
        """
        return [
            self.acceleration_mpss,
            self.steering_rate_rps
        ]

    def get_vector(self) -> np.ndarray:
        """
        Returns a two dimensional numpy array of the class fields as a vector
        """
        return np.array(
            [
                [self.acceleration_mpss],
                [self.steering_rate_rps]
            ]
        )

    @staticmethod
    def create_from_array(array: np.ndarray):
        """
        Returns a TractorInput from a numpy array of state values.
        """

        return TractorInput(
            acceleration_mpss=array[0],
            steering_rate_rps=array[1]
        )

    @staticmethod
    def create_from_list(list: List[float]):
        """
        Returns a TractorInput from a list of state values.
        """

        return TractorInput(
            acceleration_mpss=list[0],
            steering_rate_rps=list[1]
        )

    @staticmethod
    def create_from_vector(vector: np.ndarray):
        """
        Returns a TractorInput from a vector of state values represented by a two dimensional numpy array.
        """
        return TractorInput(
            acceleration_mpss=vector[0][0],
            steering_rate_rps=vector[1][0]
        )