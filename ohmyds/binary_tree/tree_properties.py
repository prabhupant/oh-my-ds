import json
from dataclasses import dataclass


@dataclass
class TreeProperties:
    """
    Class for keeping track of all tree properties
    """
    nodes: int
    leaves: int
    height: int
    levels: int
    diameter: int
    is_bst: bool
    max_val: int
    min_val: int
    is_complete: bool
    is_perfect: bool
    is_balanced: bool
    is_heap: bool
    is_max_heap: bool
    is_min_heap: bool


    def __init__(
        self,
        nodes=None,
        leaves=None,
        height=None,
        levels=None,
        diameter=None,
        is_bst=None,
        max_val=None,
        min_val=None,
        is_complete=None,
        is_perfect=None,
        is_balanced=None,
        is_heap=None,
        is_max_heap=None,
        is_min_heap=None
    ):
        self.nodes = nodes
        self.leaves = leaves
        self.height = height
        self.levels = levels
        self.diameter = diameter
        self.is_bst = is_bst
        self.max_val = max_val
        self.min_val = min_val
        self.is_complete = is_complete
        self.is_perfect = is_perfect
        self.is_balanced = is_balanced
        self.is_heap = is_heap
        self.is_max_heap = is_max_heap
        self.is_min_heap = is_min_heap


    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)


    def __str__(self):
        return self.__repr__()


    def get_properties(self):
        return self.__dict__

