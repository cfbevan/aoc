from __future__ import annotations

class Pt:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"Pt({self.x},{self.y})"

    def __add__(self, __o: Pt) -> Pt:
        return Pt(self.x + __o.x, self.y + __o.y)

    def __sub__(self, __o: Pt) -> Pt:
        return Pt(self.x - __o.x, self.y - __o.y)

    def __eq__(self, __o: Pt) -> bool:
        return self.x == __o.x and self.y == __o.y
        
    def __ne__(self, __o: Pt) -> bool:
        return self.x != __o.x or self.y != __o.y

    def __hash__(self) -> int:
        return hash((self.x,self.y))

    def __complex__(self) -> complex:
        return self.x + self.y * 1j

    def manhattan_distance(self, __o: Pt) -> int:
        return abs(self.x - __o.x) + abs(self.y - __o.y)

    