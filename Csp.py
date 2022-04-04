from typing import Dict, List, Optional
from Constraint import Constraint, V, D
import random


class Csp:
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
        self.curr_domains: Dict[V, List[D]] = {}
        self.connections: Dict[V, List[V]] = {}
        self.deleted: Dict[V, Dict[V, List[D]]] = {}
        for variable in self.variables:
            self.deleted[variable] = {}
            for variable2 in self.variables:
                self.deleted[variable][variable2] = []

    def add_constraint(self, constraint: Constraint) -> Optional[bool]:
        for variable in constraint.variables:
            if variable not in self.variables:
                return False
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.fulfill(assignment):
                return False
        return True

    def constrains_heuristics(self):
        number_of_constrains = []
        for variable in self.variables:
            number_of_constrains.append(len(self.constraints[variable]))
        self.variables = [x for _, x in sorted(zip(number_of_constrains, self.variables), reverse=True)]

    def domains_heuristics(self):
        for domain in self.domains:
            random.shuffle(self.domains[domain])

    def backtracking(self, all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {}, constraint_heuristic=True,
                     domain_heuristic=True):
        if domain_heuristic:
            self.domains_heuristics()
        if constraint_heuristic:
            self.constrains_heuristics()
        self.__backtracking(all_assignment, assignment)

    def __backtracking(self, all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {}) -> Optional[V]:
        if len(assignment) == len(self.variables):
            all_assignment.append(assignment)
            return
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.__backtracking(all_assignment, local_assignment)
                if result is not None:
                    return result

    def forward_checking(self, connections: Dict[V, List[V]], all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {},
                         constraint_heuristic=True, domain_heuristic=True):
        self.curr_domains = self.domains.copy()
        self.connections = connections
        if domain_heuristic:
            self.domains_heuristics()
        if constraint_heuristic:
            self.constrains_heuristics()
        self.__forward_checking(all_assignment, assignment)
        self.curr_domains = {}
        self.connections = []

    def __forward_checking(self, all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {}) -> Optional[V]:
        if len(assignment) == len(self.variables):
            all_assignment.append(assignment)
            return
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.curr_domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                flag = self.__extract_domains(first, local_assignment)
                if flag:
                    result = self.__forward_checking(all_assignment, local_assignment)
                    if result is not None:
                        return result
                self.__revert_deleted(first)

    def __extract_domains(self, first, local_assignment):
        flag = True
        for second in self.connections[first]:
            if second is not None:
                to_remove = []
                for value2 in self.curr_domains[second]:
                    local_assignment2 = local_assignment.copy()
                    local_assignment2[second] = value2
                    if not self.consistent(second, local_assignment2):
                        to_remove.append(value2)
                if len(to_remove) < len(self.curr_domains[second]):
                    self.deleted[first][second].extend(to_remove)
                    self.curr_domains[second] = [i for i in self.curr_domains[second] if i not in to_remove]
                else:
                    self.__revert_deleted(first)
                    flag = False
                    break
        return flag

    def __revert_deleted(self, first):
        for deleted in self.deleted[first]:
            self.curr_domains[deleted].extend(self.deleted[first][deleted])
            self.deleted[first][deleted] = []




