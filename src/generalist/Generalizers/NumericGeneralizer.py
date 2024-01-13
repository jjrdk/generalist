from typing import Any, Type

from src.generalist.Generalizers.BaseGeneralizer import BaseGeneralizer


class NumericGeneralizer(BaseGeneralizer):
    def __init__(self, step: float):
        self._step = step

    def can_handle(self, item_type: Type) -> bool:
        return item_type == float or item_type == int

    def inner_generalize(self, item: Any) -> Any:
        return round(item / self._step) * self._step

    def __str__(self):
        return "NumericGeneralizer(step={})".format(self._step)