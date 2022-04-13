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

    def domains_heuristics(self, assignment):
        values = list(assignment.values())
        set_values = set(values)
        values_amount = {}
        for value in set_values:
            values_amount[value] = values.count(value)
        for domain in self.domains:
            curr_value = []
            for value in self.domains[domain]:
                curr_value.append(values_amount.get(value, 0))
            self.domains[domain] = [x for _, x in sorted(zip(curr_value, self.domains[domain]))]
        self.curr_domains = self.domains

    def backtracking(self, all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {}, constraint_heuristic=True,
                     domain_heuristic=True) -> int:
        if domain_heuristic:
            self.domains_heuristics(assignment)
        if constraint_heuristic:
            self.constrains_heuristics()
        visited_nodes = [0]
        self.__backtracking(all_assignment, assignment, visited_nodes, domain_heuristic)
        return visited_nodes[0]

    def __backtracking(self, all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {},
                       visited_nodes: List[int] = [0], domain_heuristic=True) -> Optional[V]:
        if len(assignment) == len(self.variables):
            all_assignment.append(assignment)
            return all_assignment
        if domain_heuristic:
            self.domains_heuristics(assignment)
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        visited_nodes[0] += 1
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.__backtracking(all_assignment, local_assignment, visited_nodes, domain_heuristic)
                if result is not None:
                    return result

    def forward_checking(self, connections: Dict[V, List[V]], all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {},
                         constraint_heuristic=True, domain_heuristic=True) -> int:
        self.connections = connections
        if domain_heuristic:
            self.domains_heuristics(assignment)
        if constraint_heuristic:
            self.constrains_heuristics()
        self.curr_domains = self.domains.copy()
        visited_nodes = [0]
        self.__forward_checking(all_assignment, assignment, visited_nodes)
        self.curr_domains = {}
        self.connections = []
        return visited_nodes[0]

    def __forward_checking(self, all_assignment: List[Dict[V, D]] = [], assignment: Dict[V, D] = {}, visited_nodes: List[int] = [0]) -> Optional[V]:
        if len(assignment) == len(self.variables):
            all_assignment.append(assignment)
            return all_assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.curr_domains[first]:
            visited_nodes[0] += 1
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                flag = self.__extract_domains(first, local_assignment)
                if flag:
                    result = self.__forward_checking(all_assignment, local_assignment, visited_nodes)
                    if result is not None:
                        return result
                self.__revert_deleted(first)

    def __extract_domains(self, first, local_assignment):
        flag = True
        for value in self.connections[first]:
            if value is not None:
                to_remove = []
                for domain in self.curr_domains[value]:
                    local_assignment2 = local_assignment.copy()
                    local_assignment2[value] = domain
                    if not self.consistent(value, local_assignment2):
                        to_remove.append(domain)
                if len(to_remove) < len(self.curr_domains[value]):
                    self.deleted[first][value].extend(to_remove)
                    self.curr_domains[value] = [i for i in self.curr_domains[value] if i not in to_remove]
                else:
                    self.__revert_deleted(first)
                    flag = False
                    break
        return flag

    def __revert_deleted(self, first):
        for deleted in self.deleted[first]:
            self.curr_domains[deleted].extend(self.deleted[first][deleted])
            self.deleted[first][deleted] = []




