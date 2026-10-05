
class Move:

    def __init__(self, start, end, captured=None):

        self.start = start
        self.end = end
        self.captured = captured

    @property
    def is_capture(self):
        return self.captured is not None

    def __repr__(self):

        if self.is_capture:
            return (
                f"Move({self.start} -> {self.end}, "
                f"capture={self.captured})"
            )

        return f"Move({self.start} -> {self.end})"