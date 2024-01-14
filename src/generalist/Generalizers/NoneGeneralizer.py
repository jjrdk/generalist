from typing import Type, Any

from src.generalist.Generalizers.BaseGeneralizer import BaseGeneralizer


class NoneGeneralizer(BaseGeneralizer):
    def can_handle(self, item_type: Type) -> bool:
        return True

    def inner_generalize(self, item: Any) -> Any:
        return None

    def __str__(self):
        return "NoneGeneralizer()"
