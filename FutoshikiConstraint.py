from Csp import Constraint
from typing import Dict, Tuple


class UniqueInRowAndColumn(Constraint):
    def __init__(self, place: Tuple[int, int], n: int) -> None:
        super().__init__([place])
        self.n = n
        self.place = place

    def fulfill(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        potential_duplicates = []
        for idx in range(self.n):
            if idx != self.place[1]:
                potential_duplicates.append(assignment.get((self.place[0], idx)))
            if idx != self.place[0]:
                potential_duplicates.append(assignment.get((idx, self.place[1])))
        return not assignment[self.place] in potential_duplicates


class OneGreaterThenSecond(Constraint):
    def __init__(self, place1: Tuple[int, int], place2: Tuple[int, int], n: int) -> None:
        super().__init__([place1, place2])
        self.n = n
        self.place1 = place1
        self.place2 = place2

    def fulfill(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if assignment.get(self.place1) is None or assignment.get(self.place2) is None:
            return True
        else:
            return assignment[self.place1] > assignment[self.place2]