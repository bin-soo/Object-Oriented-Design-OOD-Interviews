# enum type for Vehicle
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99


class Vehicle:
    # Write your code here
    def __init__(self):
        pass
#

class Motorcycle(Vehicle):
    # Write your code here
    pass


class Car(Vehicle):
    # Write your code here
    pass


class Bus(Vehicle):
    # Write your code here
    pass


class Spot:
    def __init__(self):
        self.status = 0

    def set_size(self, size):
        self.size = size


class Level:
    # Write your code here
    def __init__(self, row, col):
        self.spots = [[Spot() for i in range(col)] for j in range(row)]
        for i in range(len(self.spots)):
            for j in range(0, len(self.spots[i]) // 4):
                self.spots[i][j].set_size(VehicleSize.Motorcycle)
            for j in range(len(self.spots[i]) // 4, len(self.spots[i]) // 4 * 3):
                self.spots[i][j].set_size(VehicleSize.Compact)
            for j in range(len(self.spots[i]) // 4, len(self.spots[i])):
                self.spots[i][j].set_size(VehicleSize.Large)

    def find_spot(self, size, num):
        for i in range(len(self.spots)):
            for j in range(len(self.spots[i]) - num + 1):
                status = sum([self.spots[i][t].status for t in range(j, j + num)])
                if self.spots[i][j].size == size and self.spots[i][j + num - 1].size == size and status == 0:
                    for t in range(j, j + num):
                        self.spots[i][t].status = 1
                    return [i, j]
        return None

    def unpark(self, row, col, num):
        for i in range(num):
            self.spots[row][col + i].status = 0


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.levels = []
        for i in range(n):
            self.levels.append(Level(num_rows, spots_per_row))
        self.vehicles = {}

    def find_spot(self, size, num):
        for i in range(len(self.levels)):
            level = self.levels[i]
            find = level.find_spot(size, num)
            if find != None: return [i, find[0], find[1]]
        return None

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here
        print(vehicle, type(vehicle) == Motorcycle)
        if type(vehicle) == Motorcycle:
            spot = self.find_spot(VehicleSize.Motorcycle, 1)
            if spot == None: spot = self.find_spot(VehicleSize.Compact, 1)
            if spot == None: spot = self.find_spot(VehicleSize.Large, 1)
            if spot != None: self.vehicles[vehicle] = spot
            return True if spot != None else False
        elif type(vehicle) == Car:
            spot = self.find_spot(VehicleSize.Compact, 1)
            if spot == None: spot = self.find_spot(VehicleSize.Large, 1)
            if spot != None: self.vehicles[vehicle] = spot
            return True if spot != None else False
        elif type(vehicle) == Bus:
            spot = self.find_spot(VehicleSize.Large, 5)
            if spot != None: self.vehicles[vehicle] = spot
            return True if spot != None else False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        if type(vehicle) == Motorcycle or Car:
            loc = self.vehicles[vehicle]
            self.levels[loc[0]].unpark(loc[1], loc[2], 1)
        elif type(vehicle) == Bus:
            loc = self.vehicles[vehicle]
            self.levels[loc[0]].unpark(loc[1], loc[2], 5)


level=1
num_rows=1
spots_per_row=11
parkingLot = ParkingLot(level,num_rows,spots_per_row)
parkingLot.park_vehicle("Motorcycle_1")
parkingLot.park_vehicle("Car_1")
parkingLot.park_vehicle("Car_2")
parkingLot.park_vehicle("Car_3")
parkingLot.park_vehicle("Car_4")
parkingLot.park_vehicle("Car_5")
parkingLot.park_vehicle("Bus_1")
parkingLot.unpark_vehicle("Car_5")
parkingLot.park_vehicle("Bus_1")
