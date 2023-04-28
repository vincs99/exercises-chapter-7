"""Implement verified sets."""
from numbers import Integral


class VerifiedSet(set):
    """Implement verified set instance."""

    def __init__(self, its):
        """Construct."""
        for it in its:
            self._verified(it)
        super().__init__(its)

    def _verified(self, value):
        raise NotImplementedError()

    def add(self, value):
        """Add value."""
        self._verified(value)
        return super().add(value)

    def update(self, other):
        """Update after verification."""
        for val in other:
            self._verified(val)
        return super().update(other)

    def symmetric_difference_update(self, other):
        """Symmetric diff update after verification."""
        for val in other:
            self._verified(val)
        return super().symmetric_difference_update(other)

    def union(self, *others):
        """Make union in verified type."""
        for other in others:
            for val in other:
                self._verified(val)
        type(self)(*others)

        return type(self)(super().union(*others))

    def intersection(self, *others):
        """Make union in verified type."""
        type(self)(*others)

        return type(self)(super().intersection(*others))

    def difference(self, *others):
        """Make union in verified type."""
        type(self)(*others)

        return type(self)(super().difference(*others))

    def symmetric_difference(self, other):
        """Make union in verified type."""
        return type(self)(super().union(other))

    def copy(self):
        """Make union in verified type."""
        return type(self)(super().copy())


class IntSet(VerifiedSet):
    """Create integer set instance."""

    def _verified(self, value):
        if not (isinstance(value, Integral)):
            raise TypeError(f"{type(self)} expected an integer, "
                            f"got a {type(value)}.")


class UniquenessError(KeyError):
    """Raise uniqueness error."""

    pass


class UniqueSet(VerifiedSet):
    """Create sets so that no element can be added."""

    def _verified(self, value):
        if value in self:
            raise UniquenessError("Duplicates cannot be added in UniqueSet.")
