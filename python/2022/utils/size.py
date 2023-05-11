from __future__ import annotations

class Size():

    def __init__(self, min: int = 0, max: int = 0) -> None:
        self.min = min
        self.max = max

    def __str__(self) -> str:
        return f"[{self.min},{self.max}]"

    def update(self, *vals: list[int]) -> None:
        self.min = min(self.min, *vals)
        self.max = max(self.max, *vals)

    def range(self) -> range:
        return range(self.min, self.max+1)