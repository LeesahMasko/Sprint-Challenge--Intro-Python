# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class
class Vehicle():
  pass

# FlightVehicle = Subclass of Vehicle
class FlightVehicle(Vehicle):
  pass

# Starship = Subclass of FlightVehicle
class Starship(FlightVehicle):
  pass

# Airplane = Subclass of FlightVehicle
class Airplane(FlightVehicle):
  pass

# GroudVehicle = Subclass of Vehicle
class GroundVehicle(Vehicle):
  pass

# Car = Subclass of GroudVehicle
class Car(GroundVehicle):
  pass

# Motorcycle = Subclass of GroundVehicle
class Motorcycle(GroundVehicle):
  pass
