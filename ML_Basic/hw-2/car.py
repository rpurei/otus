from base import Vehicle
from engine import Engine
import exceptions


# DONE: в модуле car создайте класс Car
# DONE: класс Car должен быть наследником Vehicle
class Car(Vehicle):
    """
    Car class successor of Vehicle class, contains Engine instance
    """

    # DONE: добавьте атрибут engine классу Car
    @property
    def engine(self):
        """the engine for car"""
        return self._engine

    @engine.setter
    def engine(self, value):
        if isinstance(value, Engine):
            self._engine = value
        else:
            raise exceptions.WrongVehicleConstruction

    # DONE: объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает
    #  на текущий экземпляр Car
    def set_engine(self, engine):
        """equips car with the engine"""
        self.engine = engine
