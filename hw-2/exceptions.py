# DONE: в модуле exceptions объявите следующие исключения: LowFuelError NotEnoughFuel CargoOverload
class LowFuelError(BaseException):
    def __str__(self):
        return f'Fuel level is too low.'


class NotEnoughFuel(BaseException):
    def __str__(self):
        return f'Fuel level is not enough.'


class CargoOverload(BaseException):
    def __str__(self):
        return f'Cargo weight exceeds the max load at units'


# my own exceptions? just for fun
class WrongEngineConstruction(BaseException):
    def __str__(self):
        return f'Engine can\'t be constructed without positive volume or pistons values '


class WrongVehicleConstruction(BaseException):
    def __str__(self):
        return f'Vehicle can\'t be constructed without positive weight, fuel_consumption or fuel values'
