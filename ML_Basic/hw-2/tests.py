import base
import car
import engine
import exceptions
import plane


def test_base():
    try:
        testing_base = base.Vehicle()
    except exceptions.WrongVehicleConstruction:
        assert True
    testing_base = base.Vehicle(weight=1.5, fuel_consumption=7.5)
    assert isinstance(testing_base, base.Vehicle)
    assert hasattr(testing_base, 'weight')
    assert hasattr(testing_base, 'started')
    assert hasattr(testing_base, 'fuel')
    assert hasattr(testing_base, 'fuel_consumption')
    assert hasattr(testing_base, 'start')
    assert hasattr(testing_base, 'move')
    try:
        testing_base.fuel = -1
    except exceptions.WrongVehicleConstruction:
        assert True
    try:
        testing_base.fuel_consumption = -1
    except exceptions.WrongVehicleConstruction:
        assert True
    try:
        testing_base.weight = -1
    except exceptions.WrongVehicleConstruction:
        assert True
    try:
        testing_base.fuel = 'ssSd46ds'
    except exceptions.WrongVehicleConstruction:
        assert True
    try:
        testing_base.fuel_consumption = None
    except exceptions.WrongVehicleConstruction:
        assert True
    try:
        testing_base.weight = 'sdsfdgsf'
    except exceptions.WrongVehicleConstruction:
        assert True


def test_base_fuel():
    testing_base = base.Vehicle(weight=1.5, fuel_consumption=7.5)
    try:
        testing_base.fuel = 0
        testing_base.start()
    except exceptions.LowFuelError:
        assert True
    testing_base.fuel = 10
    testing_base.start()
    assert testing_base.started is True


def test_base_move():
    testing_base = base.Vehicle(weight=1.5, fuel_consumption=7.5)
    try:
        testing_base.move(200)
    except exceptions.NotEnoughFuel:
        assert True
    testing_base.fuel = 15
    testing_base.move(200)
    assert testing_base.fuel == 0
    testing_base.fuel = 20.0
    testing_base.move(200)
    assert testing_base.fuel == 5.0


def test_engine():
    testing_engine = engine.Engine()
    assert isinstance(testing_engine, engine.Engine)
    assert hasattr(testing_engine, 'volume')
    assert hasattr(testing_engine, 'pistons')
    try:
        testing_engine.volume = -1
    except exceptions.WrongEngineConstruction:
        assert True
    try:
        testing_engine.pistons = 0
    except exceptions.WrongEngineConstruction:
        assert True
    try:
        testing_engine.volume = 'dfd'
    except exceptions.WrongEngineConstruction:
        assert True
    try:
        testing_engine.pistons = 'S'
    except exceptions.WrongEngineConstruction:
        assert True


def test_car():
    testing_engine = engine.Engine()
    assert isinstance(testing_engine, engine.Engine)
    testing_car = car.Car(weight=1.5, fuel_consumption=7.5)
    assert isinstance(testing_car, car.Car)
    assert hasattr(testing_car, 'set_engine')
    try:
        testing_car.set_engine('Engine')
    except exceptions.WrongVehicleConstruction:
        assert True
    testing_car.set_engine(testing_engine)
    assert hasattr(testing_car, 'engine')
    assert isinstance(testing_car.engine, engine.Engine)


def test_plane():
    testing_plane = plane.Plane(weight=150, fuel_consumption=7500, max_cargo=0)
    assert isinstance(testing_plane, plane.Plane)
    assert hasattr(testing_plane, 'cargo')
    assert hasattr(testing_plane, 'max_cargo')
    assert hasattr(testing_plane, 'load_cargo')
    assert hasattr(testing_plane, 'remove_all_cargo')
    try:
        testing_plane.max_cargo = -10
    except ValueError:
        assert True
    try:
        testing_plane.max_cargo = 'S'
    except ValueError:
        assert True
    try:
        testing_plane.cargo = -10
    except ValueError:
        assert True
    try:
        testing_plane.cargo = 'BDgdgsh'
    except ValueError:
        assert True


def test_plane_cargo():
    testing_plane = plane.Plane(weight=150, fuel_consumption=7500, max_cargo=0)
    testing_plane.max_cargo = 100
    testing_plane.cargo = 50
    try:
        testing_plane.load_cargo(100)
    except exceptions.CargoOverload:
        assert True
    testing_plane.load_cargo(50)
    assert testing_plane.cargo == 100
    assert testing_plane.remove_all_cargo() == 100
    assert testing_plane.cargo == 0