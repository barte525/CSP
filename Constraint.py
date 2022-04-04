from typing import TypeVar, Dict, List
from abc import ABC, abstractmethod

V = TypeVar('V')
D = TypeVar('D')


class Constraint(ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def fulfill(self, assignment: Dict[V, D]) -> bool:
        pass
