
import math


class LowFuelError(Exception):
    def __init__(self, position, desired_location, fuel, fuel_needed):

        self.message = f'The fuel is not enough. current plane location{position}, new location {desired_location}, current amount of fuel {fuel}, minimum amount of fuel needed {fuel_needed} \n'
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Plane:
    MAX_FUEL = 1000

    def __init__(self, position, fuel):
        self._position = position
        self._fuel = self.__check_fuel(fuel)
        self._distance = 0
        print(self.plane_status())

    @staticmethod
    def __check_fuel(fuel):
        if(fuel > Plane.MAX_FUEL):
            return 1000
        else:
            return fuel

    def plane_status(self):

        return f'Plane is at position {self._position}, travel distance is {self._distance}km and the current fuel is {self._fuel} liter (max fuel is 1000 liter) \n '

    def get_plane_fuel(self):
        return self._fuel

    def get_plane_location(self):
        return self._position

    def add_fuel(self, fuel):
        self._fuel += self.__check_fuel(fuel+self._fuel)
        print(f'added {fuel} liter')

    def __str__(self):
        return self.plane_status()

    def get_total_distance(self, desired_location):
        horizontal_distance = abs(desired_location[0]-self._position[0])
        vertical_distance = abs(desired_location[1]-self._position[1])
        return math.ceil(math.sqrt(
            vertical_distance**2+horizontal_distance**2))

    def fly(self, desired_location, fuel_per_distance=4):
        try:
            # update total distance
            total_distance = self.get_total_distance(desired_location)
            fuel_needed = int(fuel_per_distance*total_distance)
            if(self._fuel < fuel_needed):
                raise LowFuelError(
                    self._position, desired_location, self._fuel, fuel_needed)

            self._distance += total_distance
            self._position = desired_location

            print(
                f'The plane will fly to {desired_location} location,the total distance is {total_distance} \n')

        except LowFuelError as error:
            print(error.args[0])


plane_1 = Plane((0, 0), 22)
plane_1.fly((3, 4))
plane_1.add_fuel(10)
plane_1.fly((10, 10))
plane_1.fly((3, 5))
