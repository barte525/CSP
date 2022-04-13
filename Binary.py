from Csp import Csp
from typing import Dict, List, Optional, Tuple, IO
from BinaryConstraint import ThreeInRowConstraint, SameNumberOfZerosAndOnes, UniqueRowsAndColumns
import numpy as np


class Binary:
    def __init__(self, n: int, file: str = '', assignment: Dict= {}):
        self.n: int = n
        self.file: str = file
        self.assignment: Dict = assignment

    def binary(self, is_backtracking: bool, constraint_heuristic: bool, domain_heuristic: bool) -> Optional[List[Dict[Tuple[int, int], int]]]:
        variables: List[Tuple[int, int]] = []
        for x in range(self.n):
            for y in range(self.n):
                variables.append((x, y))
        domains: Dict[Tuple[int, int], List[int]] = {}
        for variable in variables:
            domains[variable] = [0, 1]
        csp: Csp[Tuple[int, int], int] = Csp(variables, domains)
        for variable in variables:
            csp.add_constraint(ThreeInRowConstraint(variable, self.n))
            csp.add_constraint(SameNumberOfZerosAndOnes(variable, self.n))
            csp.add_constraint(UniqueRowsAndColumns(variable, self.n))
        if self.file != '':
            self.read_file()
        all_assignment: Optional[List[Dict[Tuple[int, int], int]]] = []
        if is_backtracking:
            result: Optional[List[Dict[Tuple[int, int], int]]] = csp.backtracking(assignment=self.assignment,
                                                                                  all_assignment=all_assignment,
                                                                                  constraint_heuristic=
                                                                                  constraint_heuristic,
                                                                                  domain_heuristic=domain_heuristic)
        else:
            connections: Dict[Tuple[int, int], List[Tuple[int, int]]] = self.add_connections()
            result: Optional[List[Dict[Tuple[int, int], int]]] = csp.forward_checking(connections=connections,
                                                                                      assignment=self.assignment,
                                                                                      all_assignment=all_assignment,
                                                                                      constraint_heuristic=
                                                                                      constraint_heuristic,
                                                                                      domain_heuristic=domain_heuristic)
        return result

    def add_connections(self) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
        connections: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
        for x in range(self.n):
            for y in range(self.n):
                connections[(x, y)] = []
                for i in range(self.n):
                    if i != y:
                        connections[(x, y)].append((x, i))
                    if i != x:
                        connections[(x, y)].append((i, y))
        return connections

    def print_solution(self, is_backtracking: bool, constraint_heuristic: bool, domain_heuristic: bool) -> None:
        all_assignment: Optional[List[Dict[Tuple[int, int], int]]] = self.binary(is_backtracking,
                                                                                 constraint_heuristic,
                                                                                 domain_heuristic)
        print(" Number of Solutions:", len(all_assignment))
        for solution in all_assignment:
            arr: np.array = np.zeros(shape=(self.n, self.n), dtype=int)
            for variable in solution.keys():
                arr[variable] = solution[variable]
            print(arr)

    def read_file(self) -> None:
        f: IO = open(self.file, "r")
        for i in range(self.n):
            row = f.readline()
            for j in range(len(row)):
                if row[j] != 'x' and row[j] != '\n':
                    self.assignment[i, j] = int(row[j])
        f.close()
