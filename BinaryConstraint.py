from Csp import Constraint
from typing import Dict, List, Tuple


class ThreeInRowConstraint(Constraint):
    def __init__(self, place: Tuple[int, int], n: int) -> None:
        super().__init__([place])
        self.n = n
        self.place = place

    def fulfill(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        return self.check_next_two_rows(assignment) and self.check_previous_two_rows(assignment) \
               and self.check_neighbors_rows(assignment) and self.check_next_two_columns(assignment) \
               and self.check_previous_two_columns(assignment) and self.check_neighbors_columns(assignment)

    def check_next_two_rows(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if self.place[0] >= self.n - 2:
            return True
        else:
            return not (assignment[self.place] == assignment.get((self.place[0] + 1, self.place[1])) ==
                        assignment.get((self.place[0] + 2, self.place[1])))

    def check_previous_two_rows(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if self.place[0] <= 1:
            return True
        else:
            return not (assignment[self.place] == assignment.get((self.place[0] - 1, self.place[1])) ==
                        assignment.get((self.place[0] - 2, self.place[1])))

    def check_neighbors_rows(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if self.place[0] == 0 or self.place[0] == self.n - 1:
            return True
        else:
            return not (assignment[self.place] == assignment.get((self.place[0] - 1, self.place[1])) ==
                        assignment.get((self.place[0] + 1, self.place[1])))

    def check_next_two_columns(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if self.place[1] >= self.n - 2:
            return True
        else:
            return not (assignment[self.place] == assignment.get((self.place[0], self.place[1] + 1)) ==
                        assignment.get((self.place[0], self.place[1] + 2)))

    def check_previous_two_columns(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if self.place[1] <= 1:
            return True
        else:
            return not (assignment[self.place] == assignment.get((self.place[0], self.place[1] - 1)) ==
                        assignment.get((self.place[0], self.place[1] - 2)))

    def check_neighbors_columns(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        if self.place[1] == 0 or self.place[1] == self.n - 1:
            return True
        else:
            return not (assignment[self.place] == assignment.get((self.place[0] - 1, self.place[1])) ==
                        assignment.get((self.place[0] + 1, self.place[1])))


class SameNumberOfZerosAndOnes(Constraint):
    def __init__(self, place: Tuple[int, int], n) -> None:
        super().__init__([place])
        self.n = n
        self.place = place

    def fulfill(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        return self.check_row(assignment) and self.check_column(assignment)

    def check_row(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        row = []
        for idx in range(self.n):
            value_row = assignment.get((self.place[0], idx))
            if value_row is None:
                return True
            else:
                row.append(value_row)
        return row.count(0) == row.count(1)

    def check_column(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        column = []
        for idx in range(self.n):
            value_column = assignment.get((idx, self.place[1]))
            if value_column is None:
                return True
            else:
                column.append(value_column)
        return column.count(0) == column.count(1)


class UniqueRowsAndColumns(Constraint):
    def __init__(self, place: Tuple[int, int], n) -> None:
        super().__init__([place])
        self.n = n
        self.place = place

    def fulfill(self, assignment: Dict[Tuple[int, int], int]) -> bool:
        return self.check(assignment, True) and self.check(assignment, False)

    def check(self, assignment: Dict[Tuple[int, int], int], is_column) -> bool:
        current_row = []
        is_unfull = self.check_unfull(assignment, self.place[int(is_column)], current_row, is_column)
        if is_unfull:
            return True
        rows = []
        for idx in range(self.n):
            row = []
            if idx != self.place[int(is_column)]:
                if not self.check_unfull(assignment, idx, row, is_column):
                    rows.append(row)
        for row in rows:
            if current_row == row:
                return False
        return True

    def check_unfull(self, assignment: Dict[Tuple[int, int], int], idx_c: int, row: List, is_column) -> bool:
        for idx in range(self.n):
            if is_column:
                value_row = assignment.get((idx, idx_c))
            else:
                value_row = assignment.get((idx_c, idx))
            if value_row is None:
                return True
            else:
                row.append(value_row)
        return False



