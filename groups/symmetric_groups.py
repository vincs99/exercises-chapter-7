"""Implement symmetric groups."""
from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    """Implement symmetric group instance."""

    symbol = "S"

    def _validate(self, value):
        """Validate elements."""
        if not (isinstance(value, np.ndarray) and
                [i for i in range(self.n)] == sorted(value)):
            raise ValueError("Element must be an array of "
                             f"numbers from 0 to {self.n - 1}).")

    def operation(self, a, b):
        """Define operation."""
        return a[b]
