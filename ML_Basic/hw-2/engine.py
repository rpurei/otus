import exceptions
from dataclasses import dataclass


# DONE: создайте датакласс Engine в модуле engine, добавьте атрибуты volume и pistons
@dataclass
class Engine:
    """
    Engine dataclass, uses to represent power module of Car class
    """
    _volume: float = 1.0
    _pistons: int = 1

    @property
    def volume(self):
        """engine volume"""
        return self._volume

    @volume.setter
    def volume(self, value):
        if (isinstance(value, int) or isinstance(value, float)) and value > 0:
            self._volume = value
        else:
            raise exceptions.WrongEngineConstruction

    @property
    def pistons(self):
        """engine pistons quantity"""
        return self._pistons

    @pistons.setter
    def pistons(self, value):
        if (isinstance(value, int)) and value > 0:
            self._pistons = value
        else:
            raise exceptions.WrongEngineConstruction
