from .timestamp import Timestamp
from .tractor_trailer_state import TractorTrailerState


class TractorTrailerStateStamped:
    def __init__(
        self,
        tractor_trailer_state: TractorTrailerState = TractorTrailerState(),
        timestamp: Timestamp = Timestamp(),
    ):
        self.tractor_trailer_state = tractor_trailer_state
        self.timestamp = timestamp
