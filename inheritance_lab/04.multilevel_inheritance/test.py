from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle


ferrari = Car()
lambo = SportsCar()
print(lambo.move())
print(lambo.drive())
print(lambo.race())
print(ferrari.move())