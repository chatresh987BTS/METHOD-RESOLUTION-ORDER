1. Create a hierarchy of vehicles with a base class Vehicle and derived classes Car, Bicycle, and Motorcycle.
i. Define methods like start_engine and stop_engine in the base class, and override them in the derived classes.
ii. Demonstrate MRO tracing for instances of different vehicle types.
class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")
    def stop_engine(self):
        print("Vehicle engine stopped")
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")
class Bicycle(Vehicle):
    def start_engine(self):
        print("Bicycle does not have an engine")
    def stop_engine(self):
        print("Bicycle stopped")
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
    def stop_engine(self):
        print("Motorcycle engine stopped")
c = Car()
b = Bicycle()
m = Motorcycle()
c.start_engine()
c.stop_engine()
print()
b.start_engine()
b.stop_engine()
print()
m.start_engine()
m.stop_engine()
print("\nMRO Tracing")
print(Car.mro())
print(Bicycle.mro())
print(Motorcycle.mro())
