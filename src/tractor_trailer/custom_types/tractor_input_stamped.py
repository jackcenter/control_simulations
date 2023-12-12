from .timestamp import Timestamp
from .tractor_input import TractorInput


class TractorInputStamped:
    def __init__(
        self,
        tractor_input: TractorInput = TractorInput(),
        timestamp: Timestamp = Timestamp(),
    ):
        self.TractorInput = tractor_input
        self.Timestamp = timestamp
