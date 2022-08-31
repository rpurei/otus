from base import Vehicle
import exceptions


# DONE: в модуле plane создайте класс Plane
# DONE: класс Plane должен быть наследником Vehicle
class Plane(Vehicle):
    """
    Plane class, successor of Vehicle class
    """

    # DONE: добавьте атрибуты cargo и max_cargo классу Plane
    # DONE: добавьте max_cargo в инициализатор (переопределите родительский)
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    @property
    def cargo(self):
        """the mass of current plane cargo (in tons)"""
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if (isinstance(value, int) or isinstance(value, float)) and value >= 0:
            self._cargo = value
        else:
            raise ValueError

    @property
    def max_cargo(self):
        """the mass of maximal available plane cargo (in tons)"""
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, value):
        if (isinstance(value, int) or isinstance(value, float)) and value >= 0:
            self._max_cargo = value
        else:
            raise ValueError

    # DONE: объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет
    #  перегруза, и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
    def load_cargo(self, cargo_weight):
        """Checks the cargo balance and if it not exceeds the max_cargo, then allows cargo load"""
        if isinstance(cargo_weight, int) or isinstance(cargo_weight, float):
            cargo_balance = self.cargo + cargo_weight
            if cargo_balance <= self.max_cargo:
                self.cargo = cargo_balance
            else:
                raise exceptions.CargoOverload(f'Cargo weight exceeds the max load at {cargo_balance - self.max_cargo} units')
        else:
            raise ValueError

    # DONE: объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo,
    #  которое было до обнуления
    def remove_all_cargo(self):
        """Return plane cargo quantity and then unloads all cargo"""
        cargo_ret = self.cargo
        self.cargo = 0
        return cargo_ret
