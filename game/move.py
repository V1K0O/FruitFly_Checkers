class Move:

    def __init__(self, start, end, captured=None):

        self.start = start

        self.end = end

        self.captured = captured

    @property
    def is_capture(self):

        return self.captured is not None

    def __eq__(self, other):

        if not isinstance(other, Move):
            return False

        return (
            self.start == other.start
            and
            self.end == other.end
            and
            self.captured == other.captured
        )

    def __repr__(self):

        if self.is_capture:

            return (
                f"Move({self.start} -> {self.end}, "
                f"capture={self.captured})"
            )

        return f"Move({self.start} -> {self.end})"