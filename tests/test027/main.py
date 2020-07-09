from __future__ import annotations
import copy
from typing import List


class Base:

    def __init__(self, value: int) -> None:
        self._value = value
        self._child: List[Base] = []
        self._parent: Base = None

    @property
    def child(self) -> List[Base]:
        return self._child

    @child.setter
    def child(self, child: List[Base]):
        self._child = child

    @property
    def parent(self) -> Base:
        return self._parent

    def append(self, child: Base):
        self._child.append(child)

    @parent.setter
    def parent(self, parent: Base):
        self._parent = parent

    @property
    def value(self):
        return self._value


class DerivedBase(Base):

    def __init__(self, value: int, string: str) -> None:
        super().__init__(value)
        self._string = string

    @property
    def string(self):
        return self._string


if __name__ == '__main__':
    base = Base(20)

    # base.child = Base(10)
    base.append(Base(10))
    base.append(Base(12))
    base.append(Base(14))
    base.parent = Base(30)

    print(f"{base} {base.value}")
    base_copy = copy.copy(base)

    print(f"{base_copy} {base_copy.value}")
