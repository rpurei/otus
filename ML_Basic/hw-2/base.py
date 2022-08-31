import exceptions
from abc import ABC


# DONE: доработайте базовый класс base.Vehicle: добавьте атрибуты weight, started, fuel, fuel_consumption
#  со значениями по умолчанию
class Vehicle(ABC):
    """
    Base class for all vehicles, can operate by move and start

    Attributes:
        _started             shows the state of power module (why base class has no one - I don't know :-)
    """
    # DONE: добавьте инициализатор для установки weight, fuel, fuel_consumption
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = bool(started)
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def weight(self):
        """the mass of vehicle (in tons)"""
        return self._weight

    @weight.setter
    def weight(self, value):
        if (isinstance(value, int) or isinstance(value, float)) and value > 0:
            self._weight = value
        else:
            raise exceptions.WrongVehicleConstruction

    @property
    def fuel(self):
        """the fuel quantity in tank(s) of vehicle (in litres)"""
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if (isinstance(value, int) or isinstance(value, float)) and value >= 0:
            self._fuel = value
        else:
            raise exceptions.WrongVehicleConstruction

    @property
    def fuel_consumption(self):
        """consumption of vehicle power module in litres of fuel per 100 km"""
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if (isinstance(value, int) or isinstance(value, float)) and value > 0:
            self._fuel_consumption = value
        else:
            raise exceptions.WrongVehicleConstruction

    # DONE: добавьте метод start, который, если ещё не состояние started, проверяет, что топлива больше нуля,
    #  и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
    def start(self):
        """Checks the fuel level and if it positive then sets vehicle to started"""
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    # DONE: добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции,
    #  и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel
    def move(self, distance):
        """Checks if the fuel level is enough for moving then calculates the remaining fuel level"""
        fuel_balance = self.fuel - (distance / 100.0) * self.fuel_consumption
        if fuel_balance >= 0:
            self.fuel = fuel_balance
        else:
            raise exceptions.NotEnoughFuel
