from typing import TypeVar, Type, Any
from abc import ABC, abstractmethod


class BaseGeneralizer(ABC):

    @abstractmethod
    def can_handle(self, item_type: Type) -> bool:
        pass

    def generalize(self, item: Any):
        if item is None:
            return None

        if not self.can_handle(type(item)):
            raise ValueError("Cannot handle type: " + str(T))

        return self.inner_generalize(item)

    @abstractmethod
    def inner_generalize(self, item: Any) -> Any:
        pass
