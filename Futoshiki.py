from Csp import Csp
from typing import Dict, List, Optional, Tuple, IO
from FutoshikiConstraint import UniqueInRowAndColumn, OneGreaterThenSecond
import numpy as np


class Futoshiki:
    def __init__(self, n: int, file: str = '', assignment: Dict = {}):
        self.n: int = n
        self.file: str = file
        self.assignment: Dict = assignment

    def futoshiki(self, is_backtracking: bool, constraint_heuristic: bool, domain_heuristic: bool) -> \
            Optional[List[Dict[Tuple[int, int], int]]]:
        variables: List[Tuple[int, int]] = []
        for x in range(self.n):
            for y in range(self.n):
                variables.append((x, y))
        domains: Dict[Tuple[int, int], List[int]] = {}
        for variable in variables:
            domains[variable] = [i for i in range(1, self.n + 1)]
        csp: Csp[Tuple[int, int], int] = Csp(variables, domains)
        for variable in variables:
            csp.add_constraint(UniqueInRowAndColumn(variable, self.n))
        if self.file != '':
            constraint_to_add = self.read_file()
            for constraint in constraint_to_add:
                csp.add_constraint(OneGreaterThenSecond(constraint[0], constraint[1], self.n))
        all_assignment: Optional[List[Dict[Tuple[int, int], int]]] = []
        if is_backtracking:
            result: Optional[List[Dict[Tuple[int, int], int]]] = csp.backtracking(assignment=self.assignment,
                                                                                  all_assignment=all_assignment,
                                                                                  constraint_heuristic=
                                                                                  constraint_heuristic,
                                                                                  domain_heuristic=domain_heuristic)
        else:
            connections = self.add_connections()
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

    def print_solution(self, is_backtracking, constraint_heuristic, domain_heuristic) -> None:
        all_assignment: Optional[List[Dict[Tuple[int, int], int]]] = self.futoshiki(is_backtracking,
                                                                                    constraint_heuristic,
                                                                                    domain_heuristic)
        print(" Number of Solutions:", len(all_assignment))
        for solution in all_assignment:
            arr: np.array = np.zeros(shape=(self.n, self.n), dtype=int)
            for variable in solution.keys():
                arr[variable] = solution[variable]
            print(arr)

    def read_file(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        f: IO = open(self.file, "r")
        constraint_to_add: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        for i in range(0, self.n * 2):
            row: str = f.readline()
            if i % 2 == 0:
                for j in range(0, len(row), 2):
                    if row[j] != 'x' and row[j] != '\n':
                        self.assignment[i//2, j//2] = int(row[j])
                for j in range(1, len(row), 2):
                    if row[j] == '>':
                        constraint_to_add.append(((i//2, (j-1)//2), (i//2, (j+1)//2)))
                    if row[j] == '<':
                        constraint_to_add.append(((i//2, (j + 1)//2), (i//2, (j - 1)//2)))
            else:
                for j in range(len(row)):
                    if row[j] == '>':
                        constraint_to_add.append((((i-1)//2, j), ((i+1)//2, j)))
                    if row[j] == '<':
                        constraint_to_add.append((((i+1)//2, j), ((i-1)//2, j)))
        f.close()
        return constraint_to_add

