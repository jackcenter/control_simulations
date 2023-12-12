import math

from matplotlib import pyplot as plt

from tractor_trailer.custom_types.tractor_input import TractorInput
from tractor_trailer.custom_types.tractor_trailer_state import TractorTrailerState
from tractor_trailer.models.tractor_trailer_plant import (
    TractorTrailerPlant,
    TractorTrailerPlantOptions,
)


def main():
    tractor_trailer_plant_options = TractorTrailerPlantOptions(
        wheel_base_m=4.0, bogey_distance_m=8.0
    )
    tractor_trailer_plant = TractorTrailerPlant(tractor_trailer_plant_options)

    initial_tractor_trailer_state = TractorTrailerState(
        x_ordinate=0.0,
        y_ordinate=0.0,
        heading_rad=1.0,
        velocity_mps=0.0,
        steering_angle_rad=1.0,
        trailer_heading_rad=0.0,
    )

    tractor_input = TractorInput(acceleration_mpss=0.0, steering_rate_rps=0.0)

    tractor_trailer_state = initial_tractor_trailer_state
    for _ in range(0, 100):
        tractor_trailer_state = tractor_trailer_plant.simulate(
            tractor_trailer_state, tractor_input, 0.01
        )

    print(tractor_trailer_state)
    print(tractor_input)

    # TODO: make something like "plot trailer" to work all of this out
    tire_width = 2
    tire_height = 1
    back_tire_angle = 180.0 / math.pi * (tractor_trailer_state.heading_rad)
    back_tire_xy = (
        tractor_trailer_state.x_ordinate - tire_width / 2.0,
        tractor_trailer_state.y_ordinate - tire_height / 2.0,
    )

    front_tire_angle = (
        back_tire_angle + 180.0 / math.pi * tractor_trailer_state.steering_angle_rad
    )
    front_tire_xy = (
        back_tire_xy[0] + 4.0 * math.cos(tractor_trailer_state.heading_rad),
        back_tire_xy[1] + 4.0 * math.sin(tractor_trailer_state.heading_rad),
    )

    fix, ax = plt.subplots()
    

    back_tire = plt.Rectangle(
        xy=back_tire_xy,
        width=tire_width,
        height=tire_height,
        angle=back_tire_angle,
        rotation_point="center",
    )
    ax.add_artist(back_tire)

    front_tire = plt.Rectangle(
        xy=front_tire_xy,
        width=tire_width,
        height=tire_height,
        angle=front_tire_angle,
        rotation_point="center",
    )
    ax.add_artist(front_tire)

    plt.plot(
        [back_tire_xy[0] + tire_width / 2.0, front_tire_xy[0] + tire_width / 2.0],
        [back_tire_xy[1] + tire_height / 2.0, front_tire_xy[1] + tire_height / 2.0],
        "r",
    )
    
    plt.xlim(-10.0, 10.0)
    plt.ylim(-10.0, 10.0)
    plt.axis("equal")

    plt.show()


def update(frame):
    

if __name__ == "__main__":
    main()
