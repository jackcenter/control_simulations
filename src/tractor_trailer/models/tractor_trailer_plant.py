import math

import numpy as np
import scipy as sp

from ..custom_types.tractor_input import TractorInput
from ..custom_types.tractor_trailer_state import TractorTrailerState


class TractorTrailerPlantOptions:
    def __init__(self, wheel_base_m: float = 0.0, bogey_distance_m: float = 0.0):
        self.wheel_base_m = wheel_base_m
        self.bogey_distance_m = bogey_distance_m


class TractorTrailerPlant:
    def __init__(self, options: TractorTrailerPlantOptions):
        self.options = options

    def get_options(self):
        return self.options

    def simulate(
        self, initial_state: TractorTrailerState, input: TractorInput, time_step: float
    ):
        solution = sp.integrate.solve_ivp(
            self.dynamics,
            (0, time_step),
            initial_state.get_list(),
            args=(input, self.options),
        )

        return TractorTrailerState.create_from_list(solution.y[:, -1])

    @staticmethod
    def dynamics(t, x: np.array, u: TractorInput, options: TractorTrailerPlantOptions):
        state = TractorTrailerState.create_from_list(x)

        state_dynamics = TractorTrailerState(
            x_ordinate=state.velocity_mps * math.cos(state.heading_rad),
            y_ordinate=state.velocity_mps * math.sin(state.heading_rad),
            heading_rad=state.velocity_mps
            * math.tan(state.steering_angle_rad)
            / options.wheel_base_m,
            velocity_mps=u.acceleration_mpss,
            steering_angle_rad=u.steering_rate_rps,
            trailer_heading_rad=state.velocity_mps
            / options.bogey_distance_m
            * math.sin(state.heading_rad - state.trailer_heading_rad),
        )

        return state_dynamics.get_list()
